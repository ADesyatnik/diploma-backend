from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('diplomaBackend.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
