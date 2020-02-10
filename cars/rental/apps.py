from django.apps import AppConfig


class RentalConfig(AppConfig):
    name = 'rental'


    def ready(self):
        print('signals')
        import rental.signals