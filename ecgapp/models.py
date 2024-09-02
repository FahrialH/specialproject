from django.db import models    

# Create your models here.
class ECGFile(models.Model):
    file = models.FileField(upload_to='ecg_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
