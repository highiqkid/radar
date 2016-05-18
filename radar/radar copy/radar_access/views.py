from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .forms import FilterForm, NoteForm
from .models import Profile, Filter, Startup, Note, Collection

import json
import time
import datetime


STARTUP_TABLE_LENGTH = 10


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# Create your views here.
@login_required
def index(request):
    return redirect('radar_access:filter_startups')
    #return render(request, 'radar_access/index.html', {})


class FilterStartups(LoginRequiredMixin, View):
    def get(self, request, filter_form=None):
        if not filter_form:
            profile = get_profile(request.user)
            try:
                c = profile.current_filter
                filter_form = FilterForm(
                    initial={
                        'location': c.location_country,
                        'location_city': c.location_city,
                        'market': c.market,
                        'stage_min':c.stage_min,
                        'stage_max':c.stage_max,
                        'founded_min':c.founded_min,
                        'money_raised_min':c.money_raised_min,
                        'money_raised_max':c.money_raised_max,
                        'employees_min':c.employees_min,
                        'employees_max':c.employees_max
                    }
                )
            except Exception:
                filter_form = FilterForm(
                    initial={
                        'stage_max': 2,
                        'money_raised_max': 1000000,
                        'founded_min': 2011,
                        'employees_min': 1,
                        'employees_max': 25,
                        'location': 'USA',
                        'money_raised_min': 0,
                        'stage_min': 0
                    }
                )
        context = {'filter_form':filter_form}
        return render(request, 'radar_access/filter.html', context)
    
    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            profile = get_profile(request.user)
            try:
                current_filter = profile.current_filter
            except Exception:
                current_filter = Filter()
                current_filter.owner = profile
                
            current_filter.location_country = data["location"]
            current_filter.location_city = data["location_city"]
            current_filter.market = data["market"]
            
            current_filter.stage_min = data["stage_min"]
            current_filter.stage_max = data["stage_max"]
            current_filter.founded_min = data["founded_min"]
            current_filter.money_raised_min = data["money_raised_min"]
            current_filter.money_raised_max = data["money_raised_max"]
            current_filter.employees_min = data["employees_min"]
            current_filter.employees_max = data["employees_max"]
            current_filter.fetched = False
            current_filter.save()
            current_filter.result.clear()
            messages.success(request, 'Filter updated successfully.')
                
            return redirect('radar_access:filter_startups')
        else:
            return self.get(request, filter_form=form)
    
    
@login_required
def discover_startups(request):
    profile = get_profile(request.user)
    try:
        current_filter = profile.current_filter
    except Exception:
        messages.error(request, "You must create a filter before viewing the query.")
        return redirect('radar_access:filter_startups')
    
    if not current_filter.fetched:
        year_timestamp = time.mktime(
            datetime.datetime.strptime(
                str(current_filter.founded_min),
                "%Y"
            ).timetuple()
        )
        
        matched_startups = Startup.objects.filter(
            funding_rounds__gt=(int(current_filter.stage_min) - 1),
            funding_rounds__lt=(int(current_filter.stage_max) + 1),
            money_raised__gt=(int(current_filter.money_raised_min) - 1),
            money_raised__lt=(int(current_filter.money_raised_max) + 1)#,
            #founded_date__gt=(int(year_timestamp))
            #num_employees__gt=(int(data["employees_min"]) - 1),
            #num_employees__lt=(int(data["employees_max"]) + 1)
        )
        cities_list = [x for x in current_filter.location_city.split(",") if len(x) > 1]
        if len(cities_list) > 0:
            matched_startups = matched_startups.filter(city__in=cities_list)
            
        countries_list = [x for x in current_filter.location_country.split(",") if len(x) > 1]
        if len(countries_list) > 0:
            matched_startups = matched_startups.filter(country_code__in=countries_list)
            
        markets_list = [x for x in current_filter.market.split(",") if len(x) > 1]
        if len(markets_list) > 0:
            matched_startups = matched_startups.filter(market__in=markets_list)
        
        current_filter.result.add(*list(matched_startups))
        current_filter.result.remove(*list(profile.hidden.all()))
        current_filter.fetched = True
        current_filter.save()
        
        
    startups = current_filter.result.all().order_by("-is_inc5000")
    return render_startup_table(
        request,
        "radar_access/discover.html",
        startups,
        {"num_results": (startups.count(), Startup.objects.all().count())}
    )

@login_required
def my_startups(request):
    profile = get_profile(request.user)
    startups = profile.following.all()
    return render_startup_table(
        request,
        "radar_access/startups.html",
        startups,
        {}
    )

@login_required
def add_startup(request, pk=-1):
    profile = get_profile(request.user)
    startup = Startup.objects.get(id=pk)
    if request.GET.get("collection"):
        collection = Collection.objects.get(id=int(request.GET["collection"]))
        collection.startups.add(startup)
    else:
        profile.following.add(startup)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
@login_required
def remove_startup(request, pk=-1):
    profile = get_profile(request.user)
    startup = Startup.objects.get(id=pk)
    if request.GET.get("collection"):
        collection = Collection.objects.get(id=int(request.GET["collection"]))
        collection.startups.remove(startup)
    else:
        profile.following.remove(startup)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def hide_startup(request, pk=-1):
    profile = get_profile(request.user)
    startup = Startup.objects.get(id=pk)
    
    profile.hidden.add(startup)
    if profile.current_filter.fetched:
        profile.current_filter.result.remove(startup)
    profile.following.remove(startup)
    for collection in profile.collections.all():
        collection.startups.remove(startup)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class StartupDetail(LoginRequiredMixin, View):
    def get(self, request, pk=1, note_form=NoteForm()):
        startup = Startup.objects.get(id=pk)
        try:
            startup.categories = ", ".join(json.loads(startup.categories))
        except Exception:
            startup.categories = ", ".join(categories_list(startup.categories))
        short_desc = startup.description[:250]
        if len(startup.description) >= 250:
            full_desc = startup.description
            short_desc += "..."
        else:
            full_desc = None
            
        return render(
            request,
            'radar_access/startup_detail.html',
            {
                "startup":startup,
                "note_form":note_form,
                "short_desc":short_desc,
                "full_desc":full_desc
            }
        )
    
    def post(self, request, pk=1):
        form = NoteForm(request.POST)
        if form.is_valid():
            profile = get_profile(request.user)
            data = form.cleaned_data
            try:
                note = Note()
                note.startup = Startup.objects.get(pk=pk)
                note.owner = profile
                note.text = data["text"].encode("utf8")
                note.save()
                messages.success(request, 'Note added.')
            except Exception as e:
                messages.failure(request, 'Failed: %s' % e) 
                
            return redirect('radar_access:startup_detail', pk)
        else:
            return self.get(request, pk=pk, note_form=form)
        
        
def note_delete(request, pk=-1):
    Note.objects.filter(id=pk).delete()
    messages.success(request, 'Note deleted.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def login(request):
    if request.user.is_authenticated():
        return redirect("radar_access:index")
    return render(request, "radar_access/login.html", {})

def logout(request):
    auth.logout(request)
    return redirect('radar_access:index')

def my_collections(request):
    profile = get_profile(request.user)
    return render(request, "radar_access/collections.html", {"collections":profile.collections.all()})

def new_collection(request):
    profile = get_profile(request.user)
    if request.POST.get("collection_name"):
        collection = Collection()
        collection.name = request.POST["collection_name"]
        collection.owner = profile
        collection.save()
        messages.success(request, 'Created collection %s.' % collection.name)
    return redirect("radar_access:my_collections")

def filter_save(request):
    profile = get_profile(request.user)
    if request.POST.get("collection_name") or request.GET.get("collection"):
        if request.POST.get("collection_name"):
            collection = Collection()
            collection.name = request.POST["collection_name"]
            collection.owner = profile
            collection.save()
            messages.success(request, 'Created new collection from results.')
        else:
            collection = Collection.objects.get(pk=request.GET["collection"])
            messages.success(request, 'Added results to collection.')
            
        collection.startups.add(*list(profile.current_filter.result.all()))
        return redirect("radar_access:collection_detail", collection.id)
    else:
        return redirect("radar_access:discover_startups")

def collection_detail(request, pk=1):
    collection = Collection.objects.get(id=pk)
    context = {"collection":collection}
    
    if collection.startups.all().count() > 0:
        startups = collection.startups.all()
        return render_startup_table(
            request,
            "radar_access/collection_detail.html",
            startups,
            context
        )
    else:
        return render(request, "radar_access/collection_detail.html", context)
    
def collection_delete(request, pk=-1):
    Collection.objects.filter(id=pk).delete()
    return redirect("radar_access:my_collections")

def render_startup_table(request, template_name, startups, context):
    SORTING_FIELDS = ("pk", "money_raised", "name", "city", "founded_date")
    ASC = "asc"
    DESC = "desc"
    
    sorting_urls = {}
    sorting = {}
    
    sorting_by_something = False
    for field in SORTING_FIELDS:
        param_name = "sort_" + field
        sorting_urls[field] = request.path + "?" + param_name + "="
        
        if not sorting_by_something and request.GET.get(param_name) in (ASC, DESC):
            if request.GET[param_name] == ASC:
                startups = startups.order_by(field)
                sorting_urls[field] += DESC
                sorting[field] = ASC
            else:
                startups = startups.order_by("-" + field)
                sorting_urls[field] += ASC
                sorting[field] = DESC
                
            sorting_by_something = True
        else:
            sorting_urls[field] += DESC
        
    paginator = Paginator(startups, STARTUP_TABLE_LENGTH)
    page_number = 1
    if request.GET.get("page"):
        try:
            page_number = int(request.GET["page"])
        except Exception:
            pass
        
    context["startups"] = paginator.page(page_number)
    context["sorting_urls"] = sorting_urls
    context["sorting"] = sorting
    return render(request, template_name, context)

def get_profile(user):
    try:
        return user.profile
    except Exception:
        profile = Profile()
        profile.user = user
        profile.name = user.first_name + " " + user.last_name
        profile.save()
        if len(profile.name) <= 1:
            profile.name = "Guest %s" % profile.id
            profile.save()
        return profile

def categories_list(categories):
    categories = categories.split("|")
    if len(categories) > 1:
        if len(categories[0]) < 1:
            del categories[0]
        if len(categories[-1]) < 1:
            del categories[-1]
    return categories