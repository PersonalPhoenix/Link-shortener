from django.urls import path

from .views import home_page, create_uuid, redirect_by_shortened_url


urlpatterns = [
    path('', home_page, name = 'PersonalPhoenix'),
    path('create', create_uuid, name = 'PersonalPhoenix'),
    path('<str:pk>', redirect_by_shortened_url, name = 'redirect')
]