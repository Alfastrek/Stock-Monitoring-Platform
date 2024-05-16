from django.conf import settings
from django.db import models

class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Watchlist: {self.symbol}"