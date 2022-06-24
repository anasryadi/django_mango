from django.db import models

class Mango(models.Model):
    color = models.CharField(max_length=100)
    ripe = models.BooleanField()

    mango_shop = models.ForeignKey('MangoShop', related_name='mangos', on_delete=models.CASCADE, null=True)
    