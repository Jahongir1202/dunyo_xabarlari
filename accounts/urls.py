from django.urls import path
from .views import SignUpView
# accounts/urls.py

from django.urls import path
from .views import export_users_excel

urlpatterns = [
    # Boshqa URL'larni qo'shishingiz mumkin
    path('export-users-excel/', export_users_excel, name='export_users_excel'),
    path("signup/",SignUpView.as_view(),name = 'signup'),

]

