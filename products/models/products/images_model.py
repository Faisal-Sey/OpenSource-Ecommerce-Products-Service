from django.db import models

from common.base_model import BaseModel


class Image(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    image_path = models.URLField(blank=True)
    image_type = models.CharField(max_length=100, blank=True)
    image_width = models.IntegerField(default=0, blank=True, null=True)
    image_height = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
