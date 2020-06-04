import graphene
from .types import CompanyType, BusinessModelType
from .resolvers import resolve_all_companies
from diplomaBackend.models import Company, BusinessModel


class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)
    company = graphene.Field(CompanyType, id=graphene.Int())

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_company(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Company.objects.get(pk=id)

schema = graphene.Schema(query=Query)