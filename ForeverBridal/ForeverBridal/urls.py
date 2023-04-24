
from django.contrib import admin
from django.urls import path
from store.views import index, login, SignUpForms, forget_password, contact, dress, manSuit, accessories, manAccessories, earring
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

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



urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginFor), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]





# from django.contrib import admin
# from django.urls import path
# from store.views import index, login, SignUpForms, forget_password, contact, dress, manSuit, accessories, manAccessories, earring
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.views import LoginView, LogoutView
# from .forms import LoginForm

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', index),
#     path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('signin/',SignUpForms.as_view(),name="signin"),
#     path('forget-passeword/', forget_password),
#     path('contact/', contact),
#     path('dress/', dress),
#     path('manSuit/', manSuit),
#     path('accessories/', accessories),
#     path('manAccessories/', manAccessories),
#     path('earring/', earring)
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
