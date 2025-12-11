from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    experience = models.TextField()
    skills = models.TextField()
    desired_position = models.CharField(max_length=150)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

