from django.apps import AppConfig


class HeroesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marvel_heroes'
    verbose_name = 'Heroes of the marvel'
