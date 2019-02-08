from django.contrib import admin
from aws.models import (AppsDescription, ServerAwsInfo, StaticData,
                        InfraServiceInfo, InfraDatabases, InfraCicd,
                        CreateMigrations, Ec2, Rds, Cicd)


admin.site.register(AppsDescription)
admin.site.register(StaticData)
admin.site.register(InfraServiceInfo)
admin.site.register(ServerAwsInfo)
admin.site.register(InfraDatabases)
admin.site.register(InfraCicd)
admin.site.register(CreateMigrations)
admin.site.register(Ec2)
admin.site.register(Rds)
admin.site.register(Cicd)