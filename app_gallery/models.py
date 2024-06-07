from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=55, verbose_name="Title", db_index=True)
    description = models.CharField(
        max_length=355, verbose_name="Description", blank=True, null=True
    )
    image = models.ImageField(upload_to="images/gallery", verbose_name="Logo")

    def __str__(self):
        return self.title
