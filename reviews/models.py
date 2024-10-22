from django.db import models
from django.contrib.auth.models import User


class ProductReview(models.Model):

    RATING_CHOICE = [
        (1, '1 - Poor'),
        (2, '2 - Okay'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICE)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.product.name} - {self.rating} Stars by "
            f"{self.user.username}"
        )
