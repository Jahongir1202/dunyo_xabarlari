from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# accounts/views.py

from django.http import HttpResponse
from excel_response import ExcelResponse
from .models import CustomUser

def export_users_excel(request):
    users = CustomUser.objects.all()
    data = {
        'users': users,
        'headers': ['ID', 'Username', 'Email', 'Phone Number'],
        'columns': ['id', 'username', 'email', 'phone_number'],
    }
    return ExcelResponse(data, 'users.xlsx')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Create your views here.
