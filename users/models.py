from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)

    def __str__(self):
        return f"User: {self.user} - Telefono:{self.phone} - Fecha de Nacimiento:{self.birth_date} - Imagen de perfil:{self.profile_picture}"


