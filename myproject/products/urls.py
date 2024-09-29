from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LawyerViewSet, ImageTitleViewSet, BackgroundImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lawyers', LawyerViewSet)
router.register(r'image_titles', ImageTitleViewSet)
router.register(r'backgrounds', BackgroundImageViewSet)

urlpatterns = router.urls
