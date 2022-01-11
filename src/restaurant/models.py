import uuid

from django.db import models
from django.utils import timezone

from src.base_app.models import User


class Restaurant(models.Model):

    class Meta:
        db_table = "restaurants"

    guid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100, default=True)
    description = models.CharField(max_length=255, default=False)
    meta = models.JSONField()
    created_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.guid} : {self.name}"

    def save(self, *args, **kwargs):
        if self.guid:
            self.modified_at = timezone.now()

        super(Restaurant, self).save(*args, **kwargs)


class Menu(models.Model):

    class Meta:
        db_table = "menus"

    guid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    items = models.JSONField(),
    serving_day = models.DateField(),
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    meta = models.JSONField()
    created_by = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.guid} : {self.serving_day}"

    def save(self, *args, **kwargs):
        if self.guid:
            self.modified_at = timezone.now()

        super(Menu, self).save(*args, **kwargs)
