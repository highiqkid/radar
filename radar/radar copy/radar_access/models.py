from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

import json
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    name = models.CharField(max_length=100)
    following = models.ManyToManyField("Startup", related_name="followers")
    hidden = models.ManyToManyField("Startup", related_name="+")
    
    
class Filter(models.Model):
    MONEY_RAISED_CHOICES = (
        (0, '$0',),
        (100000, '$100K',),
        (500000, '$500K',),
        (1000000, '$1M',),
        (5000000, '$5M',),
        (15000000, '$15M',),
        (150000000000, '$15M+',),#15000001
    )
    
    EMPLOYEES_CHOICES = (
        (1, '1',),
        (5, '5',),
        (15, '15',),
        (25, '25',),
        (50, '50',),
        (100, '100',),
        (250, '250',),
        (251, '250+',),
    )
    
    STAGES = (
        (0, "Seed"),
        (1, "Series A"),
        (2, "Series B"),
        (3, "Series C"),
        (4, "Series D"),
    )
    
    FOUNDED_CHOICES = [(x, str(x)) for x in range(timezone.now().year - 1, 1899, -1)]
    
    owner = models.OneToOneField("Profile", related_name="current_filter")
    fetched = models.BooleanField(default=False)
    result = models.ManyToManyField("Startup")
    
    location_country = models.CharField(max_length=50)
    location_city = models.CharField(max_length=400)
    market = models.CharField(max_length=50, default="")
    
    stage_min = models.IntegerField(choices=STAGES)
    stage_max = models.IntegerField(choices=STAGES)
        
    founded_min = models.IntegerField(choices=FOUNDED_CHOICES)
    
    money_raised_min = models.IntegerField(choices=MONEY_RAISED_CHOICES)
    money_raised_max = models.IntegerField(choices=MONEY_RAISED_CHOICES)
    
    employees_min = models.IntegerField(choices=EMPLOYEES_CHOICES, default=0)
    employees_max = models.IntegerField(choices=EMPLOYEES_CHOICES, default=0)
    
    
class Collection(models.Model):
    owner = models.ForeignKey("Profile", related_name="collections")
    name = models.CharField(max_length=100)
    startups = models.ManyToManyField("Startup", related_name="collections")
    
    
class Note(models.Model):
    owner = models.ForeignKey("Profile", related_name="notes")
    startup = models.ForeignKey("Startup", related_name="notes")
    text = models.CharField(max_length=400)
    
    def __str__(self):
        return str(self.id)

    
class Startup(models.Model):
    ordering = ['-is_inc5000']
    
    STATUS = (
        ("operating", "operating"),
        ("acquired", "acquired"),
        ("closed", "closed"),
    )
    
    # Unique ID for Crunchbase
    permalink = models.CharField(max_length=100, unique=True)
    last_updated = models.IntegerField(blank=True, default=0)
    
    ### Data from initial spreadsheet tab "companies" ###
    # Basic data
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=300)
    
    # Current status
    status = models.CharField(max_length=50, choices=STATUS)
    funding_rounds = models.IntegerField()
    
    # Markets
    categories = models.CharField(max_length=300)
    market = models.CharField(max_length=50)
    
    # Location
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    state_code = models.CharField(max_length=4, blank=True)
    country_code = models.CharField(max_length=6)
    
    # Money Raised
    money_raised = models.BigIntegerField(blank=True, default=0)
    last_funding = models.IntegerField(blank=True, default=0)
    first_funding = models.IntegerField(blank=True, default=0)
    
    # Founded
    founded_date = models.IntegerField(blank=True, default=0)
    
    ### Data to be taken individually from Crunchbase's API ###
    # Basic data
    logo = models.URLField(max_length=300, blank=True)
    short_description = models.CharField(max_length=140, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    
    # Social
    twitter_url = models.URLField(max_length=200, blank=True)
    facebook_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    
    # Employees
    num_employees_min = models.IntegerField(blank=True, default=0)
    num_employees_max = models.IntegerField(blank=True, default=0)
    
    # Team
    team = models.CharField(max_length=300, blank=True)
    
    # Money
    investors = models.CharField(max_length=300, blank=True)
    
    ### Data to be taken from other sources ###
    press_mentions = models.CharField(max_length=150, blank=True)
    competitors = models.CharField(max_length=300, blank=True)
    num_employees = models.IntegerField(blank=True, default=0)
    revenue = models.CharField(max_length=30, blank=True)
    growth_percent = models.IntegerField(blank=True, default=0)
    is_inc5000 = models.BooleanField(default=False)
    
    # Sairisheek fields
    cbase_uuid = models.CharField(max_length=33, blank=True)
    angellist_id = models.IntegerField(blank=True, default=-1)
    angellist_url = models.URLField(max_length=300, blank=True)
    angellist_name = models.CharField(max_length=100, blank=True)
    
    def founded_date_string(self):
        if self.founded_date > 0:
            founded_date = datetime.datetime.fromtimestamp(self.founded_date)
            return founded_date.strftime('%b %-d, %Y')
        return "Unknown"
    
    def __str__(self):
        return self.name.encode("latin1")

class StartupRaw(models.Model):
    name = models.CharField(max_length=700)
    permalink = models.CharField(max_length=700)
    homepage_url = models.TextField(blank=True)
    category_list = models.TextField(blank=True)
    market = models.CharField(max_length=700, blank=True)
    funding = models.BigIntegerField(blank=True)
    founded_date = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    region = models.CharField(max_length=700, blank=True)
    city = models.CharField(max_length=700, blank=True)
    description = models.TextField(blank=True)
    domain = models.TextField(blank=True)
    image_url = models.TextField(blank=True)
    facebook_url = models.TextField(blank=True)
    twitter_url = models.TextField(blank=True)
    linkedin_url = models.TextField(blank=True)
    cbase_uuid = models.CharField(max_length=40, blank=True)
    angellist_id = models.IntegerField(blank=True)
    angellist_url = models.TextField(blank=True)
    angellist_name = models.CharField(max_length=700, blank=True)
    founders = models.TextField()
    competitors = models.TextField()