# Generated by Django 5.1.4 on 2024-12-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_keywordgroup_is_top14'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_french_language',
            field=models.BooleanField(default=True),
        ),
    ]
