from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path

from api.views import ApiUserModelViewSet, WareHouseModelViewSet, ProductModelViewSet, Logout

router = DefaultRouter()

router.register('ApiUser', ApiUserModelViewSet)
router.register('WareHouse', WareHouseModelViewSet)
router.register('product', ProductModelViewSet)

urlpatterns = [
   # path('ProductView/', ProductView.as_view(), name='product'),
]

urlpatterns.extend(router.urls)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.extend(router.urls)
