from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField('Pavadinimas', max_length=100, help_text="Pavadink šitą ToDo listą kaip nors originaliai")

    class Meta:
        verbose_name = 'ToDo Listas'
        verbose_name_plural = 'ToDo Listai'

    def __str__(self):
        return self.title


class ToDoItems(models.Model):
    text = models.CharField('Užduotis', max_length=300, help_text="Ką čia dabar nuveikus")
    isCompleted = models.BooleanField(null=True, default=False)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ToDo Itemas'
        verbose_name_plural = 'ToDo Itemai'

    def __str__(self):
        return self.text