# Generated by Django 5.1.4 on 2025-01-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_website_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/news/images/video_categories')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
