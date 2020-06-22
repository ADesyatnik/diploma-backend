from graphene_django import DjangoObjectType
from graphene import relay

from diplomaBackend.models import (Company, BusinessModel, Revenue, Buyer,
                                   Person, Contact, IndustryCategory,
                                   CompanyType, CompanyStatus,
                                   Employee, Role, Research, Status,
                                   Action, ActionType, Photo,)


class CompanyNode(DjangoObjectType):
    class Meta:
        model = Company
        filter_fields = {
            'legal_name': ['icontains'],
            'abbr_name': ['icontains'],
            'phone': ['icontains'],
            'employees_number': ['lte', 'gte', 'exact'],
            'contacts__person__sur_name': ['icontains'],
            'contacts__person__first_name': ['icontains'],
            'contacts__person__email': ['icontains'],
            'contacts__person__phone': ['icontains'],
            'address': ['icontains'],
            'city': ['icontains'],
            'district': ['icontains'],
            'postcode': ['exact'],
            'company_type__name': ['icontains'],
            'parent__legal_name': ['icontains'],
            'parent__abbr_name': ['icontains'],
            'parent__address': ['icontains'],
            'parent__city': ['icontains'],
            'parent__description': ['icontains'],
            'parent__employees_number': ['lte', 'gte', 'exact'],
            'parent__stock_value': ['lte', 'gte', ],
            'parent__web': ['icontains'],
            'parent__foundation_date': ['lte', 'gte', 'exact'],
            'employees_number': ['lte', 'gte', 'exact'],
            'description': ['icontains'],
            'revenue__current': ['lte', 'gte', 'exact'],
            'revenue__min_value': ['lte', 'gte', 'exact'],
            'revenue__max_value': ['lte', 'gte', 'exact'],
            'stock_value': ['lte', 'gte', ],
            'owner__person__sur_name': ['icontains'],
            'owner__person__first_name': ['icontains'],
            'owner__person__email': ['icontains'],
            'owner__person__phone': ['icontains'],
            'company_status__current_status__stage_number': ['lte', 'gte', 'exact'],
            'company_status__current_status__name': ['icontains'],
            'web': ['icontains'],
            'business_models__name': ['icontains'],
            'industry_categories__name': ['icontains'],
            'foundation_date':  ['lte', 'gte', 'exact']
        }
        interfaces = (relay.Node, )


class BusinessModelNode(DjangoObjectType):
    class Meta:
        model = BusinessModel


class RevenueNode(DjangoObjectType):
    class Meta:
        model = Revenue


class BuyerNode(DjangoObjectType):
    class Meta:
        model = Buyer


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person


class ContactNode(DjangoObjectType):
    class Meta:
        model = Contact


class IndustryCategoryNode(DjangoObjectType):
    class Meta:
        model = IndustryCategory


class CompanyTypeNode(DjangoObjectType):
    class Meta:
        model = CompanyType


class CompanyStatusNode(DjangoObjectType):
    class Meta:
        model = CompanyStatus


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee


class RoleType(DjangoObjectType):
    class Meta:
        model = Role


class ResearchType(DjangoObjectType):
    class Meta:
        model = Research


class StatusNode(DjangoObjectType):
    class Meta:
        model = Status


class ActionNode(DjangoObjectType):
    class Meta:
        model = Action


class ActionTypeNode(DjangoObjectType):
    class Meta:
        model = ActionType


class PhotoNode(DjangoObjectType):
    class Meta:
        model = Photo
