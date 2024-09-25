from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, Indexing

router = DefaultRouter()
router.register(r'logappapi', UsuarioViewSet)

urlpatterns = [
    path('routLog/', include(router.urls)),
    path('', Indexing),
]
