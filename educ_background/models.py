from django.db import models

class Elementary(models.Model):
    schoolname = models.CharField(max_length=255)
    schooladdress = models.CharField(max_length=255)
    honors = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.schoolname


class HighSchool(models.Model):
    schoolname = models.CharField(max_length=255)
    schooladdress = models.CharField(max_length=255)
    honors = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.schoolname


class SeniorHigh(models.Model):
    schoolname = models.CharField(max_length=255)
    schooladdress = models.CharField(max_length=255)
    honors = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.schoolname
