from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
#user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)

    def __str__(self):
        return self.first_name + "   " + self.last_name


class ReportSuspect(models.Model):
    genderList = (
        ('male', 'male'),
        ('female', 'female')
    )
    suspect_name = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=30, null=True)
    dresscode = models.CharField(max_length=200, null=True)
    incident_description = models.CharField(max_length=500, null=True)
    sex = models.CharField(choices=genderList, max_length=200)

    def __str__(self):
        return self.suspect_name


#class CrimeReport(models.Model):
#    STATUS_CHOICES = [
#        ('pending', 'Pending'),
#        ('solved', 'Solved'),
#    ]

#    title = models.CharField(max_length=100)
#    suspect_name = models.CharField(max_length=100)
#    description = models.TextField()
#    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
#    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#    created_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return self.title
