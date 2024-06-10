from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(upload_to="images/news/")
    documents = models.FileField(upload_to="files/news/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
    
    def __str__(self):
        return self.title
    
    def get_last_three_news(self):
        return self.objects.all().order_by('-created_at')[:3]