from django.urls import path, include

page_route = include('pages.urls')
urlpatterns = [
    path('', page_route),
    path('pages/', page_route)
]

