import graphene
from .types import CompanyNode
from .resolvers import resolve_all_companies
from diplomaBackend.models import Company
from .mutations import CompanyMutation
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
import graphql_jwt


class Query(graphene.ObjectType):
    all_companies = DjangoFilterConnectionField(CompanyNode)
    company = graphene.Field(CompanyNode, id=graphene.Int())

    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_all_companies(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return Company.objects.none()
        else:
            return Company.objects.all()

    def resolve_company(self, info, **kwargs):
        print(info.context.user)
        id = kwargs.get('id')

        if id is not None:
            if not info.context.user.is_authenticated:
                return Company.objects.none()
            else:
                return Company.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_company = CompanyMutation.Field()

    # Auth module.
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
