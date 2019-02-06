from django.contrib import admin
from aws.models import AppsDescription, ServerAwsInfo, StaticData, InfraServiceInfo, InfraDatabases, InfraCicd


admin.site.register(AppsDescription)
admin.site.register(StaticData)
admin.site.register(InfraServiceInfo)
admin.site.register(ServerAwsInfo)
admin.site.register(InfraDatabases)
admin.site.register(InfraCicd)