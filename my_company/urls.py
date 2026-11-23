from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('contacts/united-states', views.contacts_us, name='contacts-us'),
    path('contacts/canada', views.contacts_ca, name='contacts-ca'),
    path('contacts/australia', views.contacts_au, name='contacts-au'),

    path('contact/', views.contacts, name='contact-alt'),

    path('news/<path:_>/', views.news, name='news-catchall'),
    path('management/<path:_>/', views.management, name='mgmt-catchall'),
    path('about/<path:_>/', views.about, name='about-catchall'),
    path('contacts/<path:_>/', views.contacts, name='contacts-catchall'),
    path('contact/<path:_>/', views.contacts, name='contact-alt-catchall'),
]
