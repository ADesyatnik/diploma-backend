from diplomaBackend.models import Company


def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()