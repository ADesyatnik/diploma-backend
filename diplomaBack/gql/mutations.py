from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import CompanySerializer
from diplomaBackend.models import Company


class CompanyMutation(SerializerMutation):
    class Meta:
        serializer_class = CompanySerializer
        # model_operations = ['create', 'update']
        lookup_field = 'id'

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance = Company.objects.filter(
                id=input['id'],
            ).first()
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}

            else:
                raise http.Http404

        return {'data': input, 'partial': True}
