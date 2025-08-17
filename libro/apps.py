from django.apps import AppConfig


class LibroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libro'

class EditorialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'editorial'