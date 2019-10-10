from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"

    number = models.CharField(max_length=4)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Persons"

    avatar = models.ImageField(upload_to='images/avatars/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    personal_image = models.ImageField(upload_to='images/personal_images/')

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name




