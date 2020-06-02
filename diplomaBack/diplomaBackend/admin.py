from django.contrib import admin
from .models import Person, Contact, Buyer, Role, Employee, CompanyType, Revenue, Status, CompanyStatus, ActionType, Action, BusinessModel, IndustryCategory, Research, Company

# Register your models here.
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Buyer)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(CompanyType)
admin.site.register(Revenue)
admin.site.register(Status)
admin.site.register(CompanyStatus)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(BusinessModel)
admin.site.register(IndustryCategory)
admin.site.register(Research)
admin.site.register(Company)