# Generated by Django 5.1.4 on 2025-01-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_videocategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='categories',
            field=models.ManyToManyField(blank=True, to='news.videocategory'),
        ),
    ]
