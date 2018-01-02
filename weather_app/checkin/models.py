from django.db import models

class Checkin(models.Model):
    user = models.ForeignKey('user_authentication.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')

class Top(models.Model):
    checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE)
    tank = models.BooleanField(default=False)
    t_shirt = models.BooleanField(default=False)
    long_sleeve_shirt = models.BooleanField(default=False)
    sweater = models.BooleanField(default=False)
    jacket = models.BooleanField(default=False)

class Bottom(models.Model):
    checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE)
    shorts = models.BooleanField(default=False)
    jeans = models.BooleanField(default=False)
    khakis = models.BooleanField(default=False)

class Shoes(models.Model):
    checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE)
    sneakers = models.BooleanField(default=False)
    boots = models.BooleanField(default=False)
    flip_flops = models.BooleanField(default=False)
