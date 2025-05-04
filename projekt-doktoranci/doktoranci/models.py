from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Doktorant(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    temat_pracy = models.TextField()
    promotor = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('nowy', 'Nowy'),
        ('w_toku', 'W toku'),
        ('zakończony', 'Zakończony')
    ])

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class ProfilUzytkownika(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administracja'),
        ('rada', 'Rada'),
        ('sekretarz', 'Sekretarz'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rola = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.get_rola_display()})"

def get_user_role(user):
    try:
        return user.profiluzytkownika.rola
    except ProfilUzytkownika.DoesNotExist:
        return None


class PrzewodDoktorski(models.Model):
    doktorant = models.CharField(max_length=200)
    temat = models.TextField()
    promotor = models.CharField(max_length=200)
    data_zlozenia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.doktorant} — {self.temat[:50]}"
