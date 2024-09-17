# Generated by Django 5.1 on 2024-08-31 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0002_remove_dog_adoption_date_alter_dog_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='dog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='shelter',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
