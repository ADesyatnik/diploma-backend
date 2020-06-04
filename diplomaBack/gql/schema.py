import graphene
from .companies.types import CompanyType, BusinessModelType
from .companies.resolvers import resolve_all_companies
from diplomaBackend.models import Company, BusinessModel


class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)
    all_business_models = graphene.List(BusinessModelType)

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_business_models(self, info, **kwargs):
        return BusinessModel.objects.all()

schema = graphene.Schema(query=Query)