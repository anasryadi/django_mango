from django.urls import path
from .views.mangos import MangosView, MangoView
from .views.mango_shops import MangoShopsView, MangoShopView

urlpatterns = [
    path('mangos/', MangosView.as_view(), name='mangos'),
    path('mangos/<int:pk>', MangoView.as_view(), name='mango'),
    path('mango_shops/', MangoShopsView.as_view(), name='mango_shops'),
    path('mango_shops/<int:pk>', MangoShopView.as_view(), name='mango_shop')
]
