from django.db import models

from common.base_model import BaseModel


class Menu(BaseModel):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=500, blank=True)
    hidden = models.BooleanField(default=False)
    url = models.URLField(blank=True)
    path = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
