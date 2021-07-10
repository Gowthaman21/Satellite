from django.db import models

class User(models.Model):

    name = models.CharField(max_length=25, primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class  details(models.Model):
    Name = models.CharField(max_length=100)
    Country = models.CharField(max_length=50)
    ownedby = models.CharField(max_length=50)
    operator = models.CharField(max_length=100)
    users = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    detpurpose = models.CharField(max_length=50)
    orbit_class = models.CharField(max_length=50)
    orbit_type = models.CharField(max_length=50)
    GEO_longitude = models.CharField(max_length=50)
    perigee = models.CharField(max_length=50)
    apogee = models.CharField(max_length=50)
    eccentricity = models.CharField(max_length=50)
    inclination = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    launch_mass = models.CharField(max_length=50)
    dry_mass = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    launch_date = models.CharField(max_length=20)
    Expected_lifetime = models.CharField(max_length=50)
    contractor = models.CharField(max_length=50)
    country_of_contractor = models.CharField(max_length=50)
    launch_site = models.CharField(max_length=50)
    launch_vehicle = models.CharField(max_length=50)
    COSPAR_number = models.CharField(max_length=50)
    NORAD_number = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)
    orbital_data_source = models.CharField(max_length=50)
