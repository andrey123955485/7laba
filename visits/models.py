from django.db import models

class VisitCount(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Visits: {self.count}"
