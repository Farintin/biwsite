from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index', views.home, name = 'home'),
    path('services', views.services, name = 'services'),
    path('photos', views.photos, name = 'photos'),
    path('photos/<str:photo>', views.photos, name = 'photos'),
    path('videos', views.videos, name = 'videos'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('register', views.register, name = 'register')
   ]