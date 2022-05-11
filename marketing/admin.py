from django.contrib import admin
from .models import MarketingMeeting , MeetingType , Contract , ContractType
def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]

def getFieldsModel2(model):
    return ['id', 'type']
class MarketingMeetingAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(MarketingMeeting)


class MeetingTypeAdmin(admin.ModelAdmin):
    list_display = getFieldsModel2(MeetingType)


admin.site.register(MeetingType , MeetingTypeAdmin  )
admin.site.register(MarketingMeeting , MarketingMeetingAdmin  )
admin.site.register([Contract, ContractType])
# Register your models here.


