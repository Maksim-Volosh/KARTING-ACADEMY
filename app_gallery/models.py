from django.db import models
from PIL import Image

class GalleryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(image__isnull=False)

    def with_min_width(self, min_width):
        galleries = []
        for gallery in self.get_queryset():
            try:
                with Image.open(gallery.image.path) as img:
                    if img.width >= min_width:
                        galleries.append(gallery)
            except FileNotFoundError:
                continue
        return galleries

class Gallery(models.Model):
    title = models.CharField(max_length=55, verbose_name="Title", db_index=True)
    description = models.CharField(max_length=355, verbose_name="Description", blank=True, null=True)
    image = models.ImageField(upload_to="images/gallery", verbose_name="Logo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    objects = GalleryManager()

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title
    
    
