from django.db import models

class Checkin(models.Model):
    user = models.ForeignKey('user_authentication.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    temp = models.IntegerField()
    desc = models.CharField(max_length=40)

    class Meta:
        unique_together = ('user', 'date')

class Clothes(models.Model):
    checkin = models.OneToOneField(Checkin, on_delete=models.CASCADE)
    tank = models.BooleanField(default=False)
    t_shirt = models.BooleanField(default=False)
    long_sleeve_shirt = models.BooleanField(default=False)
    sweater = models.BooleanField(default=False)
    jacket = models.BooleanField(default=False)
    shorts = models.BooleanField(default=False)
    jeans = models.BooleanField(default=False)
    khakis = models.BooleanField(default=False)
    sneakers = models.BooleanField(default=False)
    boots = models.BooleanField(default=False)
    flip_flops = models.BooleanField(default=False)
