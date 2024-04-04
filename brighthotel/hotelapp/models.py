from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    class Meta():
        db_table = "Contact"


class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField()
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)

    class Meta():
        db_table = "Customer"


class admin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

    class Meta():
        db_table = "admin"


class Conventionhall(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(default=0)
    address = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    contact_number = models.BigIntegerField()
    website = models.URLField()
    email = models.EmailField()
    cost = models.IntegerField()
    amenities = models.TextField()
    seating_capacity = models.IntegerField()
    rooms_available = models.IntegerField()
    catering = models.CharField(max_length=30)

    class Meta():
        db_table = "Conventionhall"


class Rating(models.Model):
    conventionhall = models.ForeignKey(Conventionhall, on_delete=models.CASCADE)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta():
        db_table = "rating"


class Booking(models.Model):
    conventionhall1 = models.ForeignKey(Conventionhall, on_delete=models.CASCADE)
    email = models.EmailField()
    required_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    no_of_guests = models.IntegerField()
    cost = models.IntegerField()
    status = models.CharField(max_length=30, default="new")

    class Meta():
        db_table = "booking"

class Notifications(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(default=0)


    class Meta():
        db_table="Notifications"

