from rest_framework import routers

from .views import RestaurantViewSet


router = routers.SimpleRouter()
router.register("", RestaurantViewSet)
urlpatterns = router.urls
