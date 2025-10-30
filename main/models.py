from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)  # Course name (e.g. Nazra Quran)
    description = models.TextField()  # Short detail
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True)  # Date auto added
    duration = models.CharField(max_length=50, default="3 Months")
    instructor = models.CharField(max_length=100, default="AR Online Quran Academy")

    def __str__(self):
        return self.title



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"




