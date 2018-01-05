from django.db import models
from checkin.models import Checkin

class ClothesBase(models.Model):
    checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE)
    user = models.ForeignKey('user_authentication.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'checkin')

class Jeans(ClothesBase):
    def __str__(self):
        return 'Jeans'

class Shorts(ClothesBase):
    def __str__(self):
        return 'Shorts'

class Khakis(ClothesBase):
    def __str__(self):
        return 'Khakis'

class Sneakers(ClothesBase):
    def __str__(self):
        return 'Sneakers'

class Boots(ClothesBase):
    def __str__(self):
        return 'Boots'

class FlipFlops(ClothesBase):
    def __str__(self):
        return 'Flip Flops'

class Tank(ClothesBase):
    def __str__(self):
        return 'Tank'

class TShirt(ClothesBase):
    def __str__(self):
        return 'T Shirt'

class LongSleeve(ClothesBase):
    def __str__(self):
        return 'Long Sleeve'

class Sweater(ClothesBase):
    def __str__(self):
        return 'Sweater'
