from django.db import models


# country_choices = (
#     ("IND", "India"),
#     ("ENG", "England"),
#     ("AUS", "Australia"),
# )
# Create your models here.
class Country(models.Model):
    """Stores Country name in Database"""

    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class State(models.Model):
    """Stores State name in Database"""

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    """Stores District name in Database"""

    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    """Stores City name in Database"""

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    """Stores person detail in Database"""

    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
