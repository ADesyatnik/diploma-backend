from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diplomaBackend.urls')),
    path('gql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include(debug_toolbar.urls)),
]
