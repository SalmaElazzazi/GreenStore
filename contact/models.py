from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.name} - {self.email}"
