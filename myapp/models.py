from django.db import models
from django.utils import timezone
from accounts.models import User  # кастомная модель юзера

class Posts(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name="время публикации")
    edited = models.BooleanField(default=False, verbose_name="Редактирован ли?")

    def __str__(self):
        return f'{self.title} : {self.time_stamp}'

class PostAttachments(models.Model):
    name = models.CharField(verbose_name='Название файла', blank=True, null=True)
    image = models.ImageField(upload_to='files', verbose_name='Файл')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = self.image.name.split('.')[0].capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name or "Вложение"} для поста {self.post.title}'

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    responded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} откликнулся на {self.vacancy.title}"
