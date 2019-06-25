from django.forms import ModelForm, widgets

from job.models import Job


class JobForm(ModelForm):
    prefix = 'job'

    class Meta:
        model = Job
        exclude = [ 'id', 'user' ]
        widgets = {
            'company': widgets.TextInput(attrs={'class': 'form-control'}),
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'requirements': widgets.TextInput(attrs={'class': 'form-control'}),
            'status': widgets.TextInput(attrs={'class': 'form-control'})
        }
