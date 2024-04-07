from django.db import models

# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!


class Transport(models.Model):
    id_transport = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.identification

class Passenger(models.Model):
    num_identification = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.num_identification

class Ticket(models.Model):
    num_ticket = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_ticket

class Pollution(models.Model):
    pollution = models.FloatField()
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transport.id_transport} - Pollution Index: {self.pollution}"
