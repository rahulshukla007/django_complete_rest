from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewset

router = DefaultRouter()
router.register('product-abc', ProductGenericViewset, basename='products')

print("router.urls", router.urls)
urlpatterns = router.urls