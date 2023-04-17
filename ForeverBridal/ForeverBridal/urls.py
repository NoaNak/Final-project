
from django.contrib import admin
from django.urls import path
from store.views import index, login, SignUpForms, forget_password, contact, dress, manSuit, accessories, manAccessories, earring
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('signin/',SignUpForms.as_view(),name="signin"),
    path('forget-passeword/', forget_password),
    path('contact/', contact),
    path('dress/', dress),
    path('manSuit/', manSuit),
    path('accessories/', accessories),
    path('manAccessories/', manAccessories),
    path('earring/', earring)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

