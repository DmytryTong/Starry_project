from django.contrib.auth.models import AbstractUser
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Musician(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ManyToManyField(Position, related_name="musicians")

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} ({', '.join(self.position.values_list('name', flat=True))})"

class Rockband(models.Model):
    band_name = models.CharField(max_length=255)
    genres = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        related_name="rockbands"
    )
    musicians = models.ManyToManyField(Musician, related_name="rockbands")

    def __str__(self) -> str:
        return self.band_name

class Visitor(AbstractUser):

    class Meta:
        verbose_name = "visitor"
        verbose_name_plural = "visitors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Event(models.Model):
    show_time = models.DateTimeField()
    name = models.CharField(max_length=255)
    ticket_cost = models.DecimalField(decimal_places=2, max_digits=6)
    bands = models.ManyToManyField(Rockband, related_name="events")
    visitors = models.ManyToManyField(Visitor, related_name="events")

    def __str__(self) -> str:
        return self.name

class Ticket(models.Model):
    ticket_number = models.IntegerField()
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    owner = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"{self.event.name} "
                f"{self.event.show_time} "
                f"{self.event.bands}"
        )
