from django.contrib import admin
from aws.models import AppsDescription, InfraServiceInfo, ServerAwsInfo

admin.site.register(AppsDescription)
admin.site.register(InfraServiceInfo)
admin.site.register(ServerAwsInfo)