# Generated by Django 4.2.13 on 2024-06-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='images/', verbose_name='Logo')),
            ],
        ),
    ]