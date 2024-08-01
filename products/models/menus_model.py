from django.db import models

from common.base_model import BaseModel


class Menu(BaseModel):
    title = models.CharField(max_length=25)
    hidden = models.BooleanField(default=False)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
