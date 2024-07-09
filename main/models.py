from datetime import date, datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
    
class Player(models.Model):
    name = models.CharField(max_length=55, verbose_name="Name", db_index=True)
    surname = models.CharField(max_length=55, verbose_name="Surname")
    nationality = models.CharField(max_length=55, verbose_name="Nationality")
    
    def __str__(self):
        return f"{self.name} {self.surname}"

    def full_name(self):
        return self.__str__()

    def event_list(self):
        return ",\n".join([event.title for event in self.events.all()])

    full_name.short_description = "Full Name"
    event_list.short_description = "Events"


class Event(models.Model):
    title = models.CharField(
        max_length=155, verbose_name="Title of Event", db_index=True
    )
    country = models.CharField(max_length=55, verbose_name="Country of Event")
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Description"
    )
    image_of_track = models.ImageField(
        upload_to="images/Event", blank=True, null=True, verbose_name="Image of track"
    )
    logo = models.ImageField(
        upload_to="images/Event/logo",
        verbose_name="Logo of event",
        null=True
    )
    documents = models.FileField(
        upload_to="files/events/", blank=True, null=True, verbose_name="Any documents"
    )
    date_of_start = models.DateTimeField(verbose_name="Date of start", null=True)
    date_of_end = models.DateField(verbose_name="Date of end", null=True)
    players = models.ManyToManyField(
        Player,
        through="Statistics",
        related_name="events",
        verbose_name="Players who participate in the event",
        blank=True,
    )

    def __str__(self):
        return self.title

    def player_count(self):
        return self.players.count()
        
    player_count.short_description = "Number of Players"


class Statistics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="players", verbose_name="Category", null=True)
    points = models.IntegerField(
        verbose_name="Points", default=0, blank=True, null=True
    )
    lap_time = models.DecimalField(
        verbose_name="Lap time",
        max_digits=5,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ("player", "event")
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.player} in {self.event}"