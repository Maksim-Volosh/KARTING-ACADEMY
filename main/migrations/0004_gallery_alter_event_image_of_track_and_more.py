# Generated by Django 4.2.13 on 2024-06-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_partners_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='Title')),
                ('description', models.CharField(max_length=355, verbose_name='Description')),
                ('image', models.ImageField(upload_to='images/gallery', verbose_name='Logo')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='image_of_track',
            field=models.ImageField(blank=True, null=True, upload_to='images/Event', verbose_name='Image of track'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to='images/partners', verbose_name='Logo'),
        ),
    ]
