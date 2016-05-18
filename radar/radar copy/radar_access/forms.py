from django import forms

from django.forms import ModelForm

from models import Filter

class NoteForm(forms.Form):
    text = forms.CharField(max_length=400, widget=forms.Textarea, label="New Note")

class FilterForm(forms.Form):
    location = forms.CharField(
        label = "Country Code",
        required=False
    )
    
    """location = forms.ChoiceField(
        widget=forms.Select, choices=Filter.COUNTRY_CODES,
        label = "Country Code"
    )"""
    
    location_city = forms.CharField(
        label = "City",
        required=False
    )
    
    market = forms.CharField(
        required=False
    )
    
    """location_city = forms.ChoiceField(
        widget=forms.SelectMultiple(attrs={"data-role":"tagsinput"}), choices=Filter.CITY_CHOICES,
        label = "City"
    )"""
    
    stage_min = forms.ChoiceField(
        widget=forms.Select, choices=Filter.STAGES,
        label = "Currently or after stage"
    )
    stage_max = forms.ChoiceField(
        widget=forms.Select, choices=Filter.STAGES,
        label = "Currently or before stage"
    )
        
    founded_min = forms.ChoiceField(
        widget=forms.Select, choices=Filter.FOUNDED_CHOICES,
        label = "Founded after"
    )
    
    """money_raised_min = forms.ChoiceField(
        widget=forms.Select, choices=Filter.MONEY_RAISED_CHOICES
    )
    money_raised_max = forms.ChoiceField(
        widget=forms.Select, choices=Filter.MONEY_RAISED_CHOICES
    )
    
    employees_min = forms.ChoiceField(
        widget=forms.Select, choices=Filter.EMPLOYEES_CHOICES
    )
    employees_max = forms.ChoiceField(
        widget=forms.Select, choices=Filter.EMPLOYEES_CHOICES
    )"""
    
    money_raised_min = forms.IntegerField(label="Money Raised min ($)")
    money_raised_max = forms.IntegerField(label="Money Raised max ($)")
    
    employees_min = forms.IntegerField()
    employees_max = forms.IntegerField()
    
    def clean(self):
        errors = []
        if self.cleaned_data.get("stage_min") > self.cleaned_data.get("stage_max"):
            errors.append(
                forms.ValidationError("Invalid date range for stage.", code="0")
            )
        if self.cleaned_data.get("money_raised_min") > self.cleaned_data.get("money_raised_max"):
            errors.append(
                forms.ValidationError("Invalid range for money raised.", code="2")
            )
        """if int(self.cleaned_data.get("employees_min")) > int(self.cleaned_data.get("employees_max")):
            errors.append(
                forms.ValidationError("Invalid range for number of employees.", code="3")
            )"""
        if len(errors) > 0:
            raise forms.ValidationError(errors)