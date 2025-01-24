from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ovalie.news'  # Ensure this matches the app folder name
