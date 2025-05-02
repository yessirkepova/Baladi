from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 
class User(AbstractUser):
  first_name=models.CharField(max_length=150,blank=True, verbose_name='Name')
  first_name=models.CharField(max_length=150,blank=True, verbose_name='Surname')
  email = models.EmailField(unique=True,verbose_name='Email')
  phone = models.CharField(blank=True,verbose_name='phone number')
  password = models.CharField(max_length=150,verbose_name='phone number')

  USERNAME_FIELD='email'
  REQUIRED_FIELDS=['username','phone']
  def __str__(self):
    return f'{self.email}'




