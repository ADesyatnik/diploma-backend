import graphene
from .types import CompanyType, BusinessModelType
from .resolvers import resolve_all_companies
from diplomaBackend.models import Company, BusinessModel


class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

schema = graphene.Schema(query=Query)