from django.db import models


# Create your models here.

class ToDoTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    change_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        to='auth.User',
        related_name='to_do_list',
        on_delete=models.CASCADE
    )
    status = models.IntegerField()
