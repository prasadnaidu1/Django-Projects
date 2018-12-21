from django.db import models

class State(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    idno = models.IntegerField(primary_key=True)
    state_name = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class DonorRegister(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    city_name = models.ForeignKey(City,on_delete=models.CASCADE)
    email_id = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrigranizationRegister(models.Model):
    name = models.CharField(max_length=50)
    contact	= models.IntegerField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    email_id = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

