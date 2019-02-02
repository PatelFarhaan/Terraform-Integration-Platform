from django.contrib import admin
from aws.models import AppsDescription, InfraServiceInfo

admin.site.register(AppsDescription)
admin.site.register(InfraServiceInfo)