from django.db import models


class CoffeeGrinder(models.Model):
    servings = models.IntegerField(
        "Количество порций",
        blank=False,
        null=False
    )

    grind_size = models.IntegerField(
        "Размер помола",
        blank=False,
        null=False
    )

    is_switched_on = models.BooleanField(
        "Включена",
        blank=True,
        null=False,
        default=False
    )

    def __str__(self):
        return f"Количество порций: {self.servings}, размер помола: {self.grind_size}. " \
               f"Кофемолка работает - {self.is_switched_on}"
