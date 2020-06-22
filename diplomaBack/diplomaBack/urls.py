from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Harmony-CRM API')

urlpatterns = [
    url(r'api/docs/', schema_view),
    path('admin/', admin.site.urls),
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('diplomaBackend.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
