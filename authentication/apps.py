from django.apps import AppConfig  # ← yeh line zaroori hai

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'