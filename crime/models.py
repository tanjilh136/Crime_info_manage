from django.db import models

# from datetime import datetime

# Create your models here.


# crimes = (
#     ('Murder', 'Murder'), 
#     ('attemp to Murder', 'attemp to Murder'),
#     ('Domestic Abuse', 'Domestic Abuse'),
#     ('Child Abuse', 'Child Abuse'),
#     ('Roberry', 'Roberry'),
#     ('Fraud', 'Fraud'),
#     ('Hate Crime', 'Hate Crime'),
#     ('Harrasement', 'Harrasement'),
#     ('Sexual Harrasement', 'Sexual Harrasement'),
#     ('Rape/Sexual Assualt', 'Rape/Sexual Assualt'),
#     ('Violent Crime', 'Violent Crime'),
#     ('Terrorism', 'Terrorism'),
#     ('Anti-social Behaviour', 'Anti-social Behaviour'),
#     ('Theft', 'Theft'),
#     ('Cyber Crime / Online Fraud', 'Cyber Crime / Online Fraud'),
    

# )

class fileing(models.Model):

# Complaint's Information:
    cName = models.CharField(max_length=100)
    cRoad_Block_Sector= models.CharField(max_length=200)
    cCity_Village_House= models.CharField(max_length=200)
    cPost_Office= models.CharField(max_length=100)
    cPostal_Code= models.CharField(max_length=100)
    cDistrict=models.CharField(max_length=100)
    cPolice_Station= models.CharField(max_length=100)
    cCountry= models.CharField(max_length=100)

# Case's Details
    # Choose_Crime= models.CharField(choices=crimes)
    Choose_Crime= models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Crime_Descrip = models.TextField()

# Suspect's Information:
    sName= models.CharField(max_length=100)
    sRoad_Block_Sector= models.CharField(max_length=100)
    sCity_Village_House= models.CharField(max_length=100)
    sPost_Office= models.CharField(max_length=100)
    sPostal_Code= models.CharField(max_length=100)
    sDistrict= models.CharField(max_length=100)
    sPolice_Station= models.CharField(max_length=100)
    sCountry= models.CharField(max_length=100)


    def __str__(self):
        return self.cName
