from django.db import models
#
from model_utils.models import TimeStampedModel
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
#
from datetime import datetime
#
from django.utils import timezone
#
import uuid

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=100)
    date_birth = models.DateField('Fecha nacimiento', blank=True, null=True)
    address = models.CharField('Direccion de Recidencia', max_length=50, blank=True, null=True)
    phone = models.CharField('Telefono', max_length=10,  blank=True, null=True)
    qr_code = models.FileField(upload_to="qr/", blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    otpauth_url = models.CharField(max_length=225, blank=True, null=True)
    otp_base32 = models.CharField(max_length=255, null=True)
    qr_code = models.ImageField(upload_to="qrcode/",blank=True, null=True)
    login_otp = models.CharField(max_length=255, null=True, blank=True)
    login_otp_used = models.BooleanField(default=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    is_staff = models.BooleanField('Pertenece al staff', default=False)
    is_active = models.BooleanField('Usuario activo', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]

    def is_valid_otp(self):
        #lifespan_in_seconds = 59
        #now = datetime.now(timezone.utc)
        #time_diff = now - self.otp_created_at
        #time_diff = time_diff.total_seconds()
        #if time_diff >= lifespan_in_seconds or self.login_otp_used :
        #    return False
        return True



    def get_full_name(self):
        return self.full_name
    

    def get_email(self):
        return self.email
