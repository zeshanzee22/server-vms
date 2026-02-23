from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceTypeViewSet, AlertTypeViewSet, WarningTypeViewSet, LoginView

router = DefaultRouter()
router.register(r'device-types', DeviceTypeViewSet)
router.register(r'alert-types', AlertTypeViewSet)
router.register(r'warning-types', WarningTypeViewSet)

urlpatterns = [
    # ModelViewSet APIs
    path('', include(router.urls)),
    # Login API
    path('login/', LoginView.as_view(), name='login'),
]