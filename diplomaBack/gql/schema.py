import graphene
from .types import CompanyNode
from .resolvers import resolve_all_companies
from diplomaBackend.models import Company
from .mutations import CompanyMutation
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    all_companies = DjangoFilterConnectionField(CompanyNode)
    company = graphene.Field(CompanyNode, id=graphene.Int())

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_company(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Company.objects.get(pk=id)

class Mutation(graphene.ObjectType):
    create_company = CompanyMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)