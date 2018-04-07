import datetime

from django.db import models

# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class SiteInfo(models.Model):
    site = models.ForeignKey(Site, related_name='details', on_delete=models.CASCADE)
    a_value = models.DecimalField(max_digits=19, decimal_places=2)
    b_value = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.site.title + " : " + self.date.strftime("%m/%d/%y")