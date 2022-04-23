from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_def),
    path('logout/', views.logout_def),
    path('registration/', views.registration),
    path('',views.index)
]