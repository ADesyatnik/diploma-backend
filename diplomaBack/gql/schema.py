import graphene
from .types import (CompanyNode, BusinessModelNode,
                    IndustryCategoryNode, PersonNode, ContactNode,
                    StatusNode)
from diplomaBackend.models import (
    Company, BusinessModel, IndustryCategory, Person, Contact,
    Status)
from .mutations import CompanyMutation
from graphene_django.debug import DjangoDebug
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphql import GraphQLError
from django.db.models import Count

from graphene_django.filter import DjangoFilterConnectionField


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_companies = DjangoFilterConnectionField(CompanyNode)
    company = graphene.Field(CompanyNode, id=graphene.Int())

    
    business_models = graphene.List(BusinessModelNode)
    industry_categories = graphene.List(IndustryCategoryNode)
    owners = graphene.List(ContactNode)
    all_statuses = graphene.List(StatusNode)

    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_all_companies(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise GraphQLError('Not logged in!')
        else:
            return Company.objects.all()

    def resolve_company(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            if not info.context.user.is_authenticated:
                return Company.objects.none()
            else:
                return Company.objects.get(pk=id)

    def resolve_business_models(self, info, **kwargs):
        return BusinessModel.objects.all()

    def resolve_industry_categories(self, info, **kwargs):
        return IndustryCategory.objects.all()

    def resolve_owners(self, info, **kwargs):
        return Contact.objects.exclude(owned_companies=None)

    def resolve_all_statuses(self, info, **kwargs):
        return Status.objects.all()

class Mutation(graphene.ObjectType):
    create_company = CompanyMutation.Field()

    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
