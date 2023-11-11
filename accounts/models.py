from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator,EmailValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, validators=[MinValueValidator(18, message="Siz 18 yoshdan kichik bo'lgansiz")])

    # Additional fields
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Noto'g'ri e-mail formati")])
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Noto'g'ri telefon raqami formati")])

# Rest of your code
