from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True
    )
    name = models.CharField(
        max_length=50
    )
    image = models.CharField(
        max_length=50
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    release_date = models.DateField()
    lte_exists = models.CharField(
        max_length=10
    )
    slug = models.SlugField(
        max_length=50
    )

