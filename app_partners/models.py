from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=55, verbose_name="Name")
    logo = models.ImageField(upload_to="images/partners", verbose_name="Logo")

    def __str__(self):
        return self.name
