from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=55, verbose_name='Name')
    surname = models.CharField(max_length=55, verbose_name='Surname')
    nationality = models.CharField(max_length=55, verbose_name='Nationality')

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def full_name(self):
        return self.__str__()
    
    def event_list(self):
        return ',\n'.join([event.title for event in self.events.all()])
    
    full_name.short_description = 'Full Name'
    event_list.short_description = 'Events'
    

class Event(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title of Event')
    country = models.CharField(max_length=55, verbose_name='Country of Event')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Description')
    image_of_track = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Image of track')
    documents = models.FileField(upload_to='files/', blank=True, null=True, verbose_name='Any documents')
    date_of_start = models.DateField(verbose_name='Date of start')
    date_from = models.DateField(verbose_name='Date from')
    date_to = models.DateField(verbose_name='Date to')
    players = models.ManyToManyField(Player, related_name='events', verbose_name='Players who participate in the event')

    def __str__(self):
        return self.title

    def player_count(self):
        return self.players.count()
    
    player_count.short_description = 'Number of Players'
