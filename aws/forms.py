from django import forms
from aws.models import AppsDescription, InfraServiceInfo, InfraDatabases, InfraCicd, CreateMigrations



class DashboardForm(forms.ModelForm):
    class Meta():
        model = AppsDescription
        widget = {'plan_to_migrate': forms.RadioSelect}
        exclude = ["server_names", "create_app_response"]



class InfraForm(forms.ModelForm):

    class Meta():
        model = InfraServiceInfo
        exclude = ['app_id']



class InfraDatabase(forms.ModelForm):

    class Meta():
        model = InfraDatabases
        exclude = ['env_id']


class InfraCicds(forms.ModelForm):

    class Meta():
        model = InfraCicd
        exclude = ['app_id']


class CreateMigrationForm(forms.ModelForm):

    class Meta():
        model = CreateMigrations
        fields = '__all__'