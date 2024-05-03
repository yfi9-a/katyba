# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(SoldierAdmin)
admin.site.register(Soldier)
admin.site.register(SoldierArmyUnits)
admin.site.register(SoldierPunishments)
admin.site.register(Vacations)
admin.site.register(Promotion)
admin.site.register(Rewards)

admin.site.register(Officer)
admin.site.register(OfficerArmyUnits)
admin.site.register(OfficerPunishments)
admin.site.register(OfficerVacations)
admin.site.register(OfficerPromotion)
admin.site.register(Officer_Rewards)

admin.site.register(Sub_officer)
admin.site.register(Sub_officerArmyUnits)
admin.site.register(Sub_officerPunishments)
admin.site.register(Sub_officer_Vacations)
admin.site.register(Sub_officer_Promotion)
admin.site.register(Sub_officer_Rewards)

admin.site.register(Company)
admin.site.register(Squad)