from django.contrib import admin
from django.contrib.admin.sites import site
from .models import concertModel,locationModel,timefieldModel,TicketModel

class ticket_Admin(admin.ModelAdmin):
    pass 


admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timefieldModel)
admin.site.register(TicketModel)



