from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'
    verbose_name = 'Dodawanie obrazów'

    def ready(self):
        #Import procedur obsługi sygnałów.
        import images.signals
