from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("shop/", views.shop, name="shop"),
path("cart/", views.cart, name="cart"),
path("contact/", views.contact, name="contact"),
path("info/", views.info, name="info"),
path("shop/pc1/", views.pc1, name="pc1"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)