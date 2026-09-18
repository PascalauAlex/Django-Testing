from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    pass

class Product(models.Model):
    # name , price , stock_count
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(default=0)

    class Meta:
        """
            Model constraint throws an IntegrityError
            if the model is created without respecting the constraints
        """
        constraints =[
            models.CheckConstraint(
                condition=models.Q(price__gt=0),
                name="price_gt_0"
            ),
            models.CheckConstraint(
                condition=models.Q(stock_count__gt=0),
                name="stock_count_gt_0"
            )
        ]


    @property
    def in_stock(self) -> bool:
        return self.stock_count > 0

    def get_discounted_price(self, discount_percentage : int):
        """ Calculate and return the discounted price """
        return self.price * (1 - discount_percentage / 100)




