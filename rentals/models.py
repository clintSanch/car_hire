from django.db import models
class Car(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
# Create your models here.
class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"

        