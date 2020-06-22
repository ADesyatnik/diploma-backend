from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='Harmony-CRM API')

urlpatterns = [
    url(r'api/docs/', schema_view),
    url(r'^api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('diplomaBackend.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
