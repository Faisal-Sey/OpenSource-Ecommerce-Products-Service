from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        abstract = True
