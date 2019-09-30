from django.db import models

class Kelas(models.Model):  
    nama_kelas = models.CharField(max_length=100)  
    class Meta:  
        db_table = "kelas" 

class Abstract(models.Model):
    abstract = models.CharField(max_length=2000) 
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    class Meta:
        db_table = "abstract"
