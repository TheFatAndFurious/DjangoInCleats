# Generated by Django 5.1.4 on 2025-01-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_keywordgroup_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(blank=True, max_length=50)),
                ('round_number', models.IntegerField(blank=True)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(blank=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('score_home', models.IntegerField(blank=True)),
                ('score_away', models.IntegerField(blank=True)),
            ],
        ),
    ]
