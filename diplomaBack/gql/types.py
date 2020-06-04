from graphene_django import DjangoObjectType
from diplomaBackend.models import (Company, BusinessModel, Revenue, Buyer,
                                   Person, Contact, IndustryCategory,
                                   CompanyType, CompanyStatus,
                                   Employee, Role, Research, Status,
                                   Action, ActionType, Photo,)


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class BusinessModelType(DjangoObjectType):
    class Meta:
        model = BusinessModel


class RevenueType(DjangoObjectType):
    class Meta:
        model = Revenue


class BuyerType(DjangoObjectType):
    class Meta:
        model = Buyer


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class IndustryCategoryType(DjangoObjectType):
    class Meta:
        model = IndustryCategory


# class CompanyTypeType(DjangoObjectType):
#     class Meta:
#         model = CompanyType


class CompanyStatusType(DjangoObjectType):
    class Meta:
        model = CompanyStatus


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class RoleType(DjangoObjectType):
    class Meta:
        model = Role


class ResearchType(DjangoObjectType):
    class Meta:
        model = Research


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


class ActionType(DjangoObjectType):
    class Meta:
        model = Action


# class ActionTypeType(DjangoObjectType):
#     class Meta:
#         model = ActionType


class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo
