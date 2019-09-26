from django.db import models
from datetime import date


class Currency(models.Model):
    iso_code = models.CharField(
        max_length=3,
        blank=False,
        unique=True)

    class Meta:
        ordering = ('iso_code',)

    def __str__(self):
        return self.iso_code


class Country(models.Model):
    name = models.CharField(
        max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=250)
    country = models.ForeignKey(
        Country,
        related_name='cities',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    country = models.ForeignKey(
        Country,
        related_name='transactions',
        on_delete=models.SET_NULL,
        null=True)
    city = models.ForeignKey(
        City,
        related_name='transactions',
        on_delete=models.SET_NULL,
        null=True)
    currency = models.ForeignKey(
        Currency,
        related_name='transactions',
        on_delete=models.SET_NULL,
        null=True)
    amount = models.DecimalField(
        max_digits=17,
        decimal_places=2)
    transaction_time = models.DateTimeField(
        auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='transactions',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('-transaction_time',)

    def __str__(self):
        return self.currency, self.amount
