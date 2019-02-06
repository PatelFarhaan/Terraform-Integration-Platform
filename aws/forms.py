from django import forms
from aws.models import AppsDescription, InfraServiceInfo, InfraDatabases, InfraCicd



class DashboardForm(forms.ModelForm):
    class Meta():
        model = AppsDescription
        widget = {'plan_to_migrate': forms.RadioSelect}
        exclude = ["server_names", "create_app_response"]



class InfraForm(forms.ModelForm):
    class Meta():
        model = InfraServiceInfo
        fields = '__all__'



class InfraDatabase(forms.ModelForm):

    class Meta():
        model = InfraDatabases
        fields = '__all__'


class InfraCicds(forms.ModelForm):

    class Meta():
        model = InfraCicd
        fields = '__all__'