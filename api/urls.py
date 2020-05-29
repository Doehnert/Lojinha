from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import ItemListCreateView


urlpatterns = [
    path('', ItemListCreateView.as_view(), name='test'),
    path('token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls'))
]
