from django.urls import path

from .views import autorize
urlpatterns = [
    path('', autorize),
]