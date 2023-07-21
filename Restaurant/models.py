from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Reserva(models.Model):
    name = models.CharField(max_length=255)
    no_guest = models.IntegerField(default=6)
    booking_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name