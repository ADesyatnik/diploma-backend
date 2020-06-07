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
        filter_fields = '__all__'
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
