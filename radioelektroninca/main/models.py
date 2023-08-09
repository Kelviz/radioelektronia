from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField("Имя",max_length=50)
    email = models.CharField("Эл.почта",max_length=50)
    subject = models.CharField("Тема",max_length=50)
    text = models.TextField("Сообщение")

    def __str__(self) -> str:
        return self.subject
    
    #переименование в админпанали название таблицы
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"