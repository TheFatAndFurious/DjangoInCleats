# Generated by Django 5.1.4 on 2024-12-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_keywordgroup_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordgroup',
            name='is_top14',
            field=models.BooleanField(default=False),
        ),
    ]
