from django.contrib import admin
from aws.models import AppsDescription, InfraServiceInfo, ServerAwsInfo, StaticData


admin.site.register(StaticData)
admin.site.register(ServerAwsInfo)
admin.site.register(AppsDescription)
admin.site.register(InfraServiceInfo)