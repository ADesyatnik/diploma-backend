from graphene_django import DjangoObjectType
from diplomaBackend.models import Company, BusinessModel


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company

class BusinessModelType(DjangoObjectType):
    class Meta:
        model = BusinessModel

