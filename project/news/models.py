from django.db import models
from users.models import User
# Create your models here.


class Articles(models.Model):
    title = models.CharField("Название", max_length=75,)
    anons = models.CharField("Анонс", max_length=250,)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости "
