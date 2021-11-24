from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, null=False, default="")
    photo = models.ImageField()
    qisqacha_malumot = models.CharField(max_length=2000, null=False, default="")
    toliq_malumot = models.CharField(max_length=5000, null=False, default="")
    vaqti = models.DateTimeField(auto_now_add=True)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
