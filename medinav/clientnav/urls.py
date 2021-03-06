from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('invalidDevice/', views.get_invalid_device, name = 'invalidDevice'),
    path('index/', views.get_index, name='get_index'),
    path('help/', views.get_help, name='help'),
    path('selectmix/', views.get_selectmix, name='selectmix'),
    path('showmix/', views.get_showmix, name='showmix'),
    path('forgotpwd/', views.reset_pwd, name='forgotpwd'),
    path('createuser/', views.create_user, name='createuser'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

