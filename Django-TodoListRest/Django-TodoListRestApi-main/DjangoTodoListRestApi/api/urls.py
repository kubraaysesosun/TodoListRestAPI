from django.urls import path, include
from rest_framework import routers

from todo.resources.views import TodoViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('rest_auth.urls')),
    path('v1/auth/registration', include('rest_auth.registration.urls'))
]