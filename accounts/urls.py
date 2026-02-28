from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'api/profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls