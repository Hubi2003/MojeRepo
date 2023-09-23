

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notatek, name='lista_notatek'),
    path('dodaj/', views.dodaj_notatke, name='dodaj_notatke'),
    path('usun/<int:notatka_id>/', views.usun_notatke, name='usun_notatke'),
    path('notatka/<int:notatka_id>/', views.notatka_szczegoly, name='notatka_szczegoly'),
    path('ulubione/', views.lista_ulubionych, name='lista_ulubionych'),
    path('dodaj_do_ulubionych/<int:notatka_id>/', views.dodaj_do_ulubionych, name='dodaj_do_ulubionych'),
    path('usun_z_ulubionych/<int:notatka_id>/', views.usun_z_ulubionych, name='usun_z_ulubionych'),

]
