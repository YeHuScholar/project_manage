from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(default="项目名称：xxx", max_length=50)
    describe = models.TextField(default="在这里写项目描述")
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    # id = models.UUIDField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

