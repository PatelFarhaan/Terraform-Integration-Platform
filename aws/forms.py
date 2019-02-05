from django import forms
from aws.models import AppsDescription, InfraServiceInfo



class DashboardForm(forms.ModelForm):
    class Meta():
        model = AppsDescription
        widget = {'plan_to_migrate': forms.RadioSelect}
        exclude = ["server_names", "create_app_response"]


class InfraForm(forms.ModelForm):
    class Meta():
        model = InfraServiceInfo
        fields = '__all__'