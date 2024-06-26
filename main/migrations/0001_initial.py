# Generated by Django 4.2.13 on 2024-06-02 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Title of Event')),
                ('country', models.CharField(max_length=55, verbose_name='Country of Event')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('image_of_track', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image of track')),
                ('documents', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Any documents')),
                ('date_of_start', models.DateField(verbose_name='Date of start')),
                ('date_from', models.DateField(verbose_name='Date from')),
                ('date_to', models.DateField(verbose_name='Date to')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Name')),
                ('surname', models.CharField(max_length=55, verbose_name='Surname')),
                ('nationality', models.CharField(max_length=55, verbose_name='Nationality')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(blank=True, default=0, null=True, verbose_name='Points')),
                ('lap_time', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Lap time')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player')),
            ],
            options={
                'unique_together': {('player', 'event')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='events', through='main.Statistics', to='main.player', verbose_name='Players who participate in the event'),
        ),
    ]
