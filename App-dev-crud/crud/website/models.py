from django.db import models

# Create your models here.
class Record(models.Model):
    Created_at = models.DateTimeField(auto_now_add=True) # timestamp
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    USN = models.CharField(max_length=50)
    Program = models.CharField(max_length=50)
    Course_code = models.CharField(max_length=15)
    To_do = models.CharField(max_length=100)
    Deadline = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)  
    
    def __str__(self):
        return(f"{self.First_name} {self.Last_name}")
