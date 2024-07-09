from django.db import models

class Track(models.Model):
    track = models.CharField(max_length=55, verbose_name="Track")
    image = models.ImageField(upload_to="images/tracks", verbose_name="Image")

    def __str__(self):
        return self.track
