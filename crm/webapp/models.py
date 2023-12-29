from django.db import models

class Record(models.Model):
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
        return self.suspect_Name


#class wantedSuspect(models.Model):
#    genderList = (
#        ('male', 'male'),
#        ('female', 'female')
#    )

#    name = models.CharField(max_length=200, null=True)
#    age = models.CharField(max_length=200, null=True)
#    picture = models.ImageField(max_length=200, null=True)
#	 sex = models.CharField(choices=genderList, max_length=200)
#    datePosted = models.DateTimeField(auto_now=True)

#   def __str__(self):
#       return self.name
