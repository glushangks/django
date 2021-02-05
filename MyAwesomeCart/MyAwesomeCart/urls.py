"""MyAwesomeCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('welcome/',views.welcome,name="welcome"),
    path('about/',views.about,name="About us"),
    path('contact/',views.contact ,name="Contact"),
    path('tracker/',views.tracker ,name="Tracker"),
    path('search/',views.search ,name="Search"),
    path('productview/',views.productview ,name="Productview"),
    path('checkout/',views.checkout ,name="Checkout"),
    path('cart/',views.addtocart,name="cart"),
    path('viewall/',views.viewall,name="viewall"),
    path('delete/',views.delete,name="delete"),
    path('bay/',views.bay,name="bay"),
    path('save/',views.save,name="save"),
    path('gul/',views.gul,name="gul")


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)