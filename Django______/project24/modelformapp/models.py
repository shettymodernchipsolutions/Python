from django.db import models


# Create your models here.
class StudentTable(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    mail_id = models.EmailField()
    phone_number = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

        def __str__(self):
            return self.name