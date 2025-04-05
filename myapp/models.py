from django.db import models
from django.utils import timezone

class Posts(models.Model):
  #author
  title= models.CharField(verbose_name='Заголовок', max_length=255 )
  content= models.TextField(verbose_name='Контент')
  time_stamp=models.DateTimeField(default=timezone.now, verbose_name="время публикаций")
  edited=models.BooleanField(default=False,verbose_name="редактирован ли ?")
