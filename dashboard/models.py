from django.db import models
from django.contrib.auth.models import User
from users.models import Profiles


# Create your models here.
class Transactions(models.Model):
    transaction_title = models.CharField(max_length=50)  # Aumentei para 50 caracteres
    transaction_type = models.CharField(max_length=10)  # "income" ou "expense" talvez?
    transaction_date = models.DateField()  # Melhor que CharField para datas
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2)  # Aumentei para valores maiores
    transaction_observation = models.TextField(max_length=200, blank=True, null=True)  # TextField para textos maiores
    transaction_category = models.CharField(max_length=30)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)



