from django.db import models

class DriverInfo(models.Model):
    driverName = models.CharField(max_length=100)
    vehicleId = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    carrierName = models.CharField(max_length=100)
    mainOffice = models.CharField(max_length=200)
    homeTerminal = models.CharField(max_length=200)
    milesDrivingToday = models.CharField(max_length=50)
    totalMileageToday = models.CharField(max_length=50)
    truckNumber = models.CharField(max_length=50)
    trailerNumber = models.CharField(max_length=50)
    licensePlate = models.CharField(max_length=50)
    manifestNumber = models.CharField(max_length=100)
    shippingDocs = models.CharField(max_length=100)
    shipperCommodity = models.CharField(max_length=100)
    recapA = models.CharField(max_length=50)
    recapB = models.CharField(max_length=50)
    recapC = models.CharField(max_length=50)
    recapD = models.CharField(max_length=50)
    recapE = models.CharField(max_length=50)
    recapF = models.CharField(max_length=50)
    recapG = models.CharField(max_length=50)
    recapH = models.CharField(max_length=50)
    recapI = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.driverName} - {self.date}"