from django import forms
from .models import Elementary, HighSchool, SeniorHigh

class ElementaryForm(forms.ModelForm):
    class Meta:
        model = Elementary
        fields = ['schoolname', 'schooladdress', 'honors']


class HighSchoolForm(forms.ModelForm):
    class Meta:
        model = HighSchool
        fields = ['schoolname', 'schooladdress', 'honors']


class SeniorHighForm(forms.ModelForm):
    class Meta:
        model = SeniorHigh
        fields = ['schoolname', 'schooladdress', 'honors']
