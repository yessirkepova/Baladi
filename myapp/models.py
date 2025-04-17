from django.db import models
from django.utils import timezone

class Posts(models.Model):
  #author
  title= models.CharField(verbose_name='Заголовок', max_length=255 )
  content= models.TextField(verbose_name='Контент')
  time_stamp=models.DateTimeField(default=timezone.now, verbose_name="время публикаций")
  edited=models.BooleanField(default=False,verbose_name="редактирован ли ?")
  def __str__(self):
    return f'{self.title}:{self.time_stamp}'



class PostAttachments(models.Model):
  name=models.CharField(verbose_name='name of picture' ,blank=True, null=True)
  image=models.ImageField(upload_to='files', verbose_name='FILEE')
  post=models.ForeignKey(Posts,on_delete=models.CASCADE)

  def save(self,*args,**kwargs):
    self.name=self.image.name.split('.')[0].capitalize()
    super().save(*args,**kwargs)