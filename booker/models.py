from django.db import models
import datetime



class TypeCoworking(models.Model):
    TYPE_COWORKING = [
        ("fix", "Фиксированное рабочее место"),
        ("room", "Офис"),
        ("free", "Свободное место")
    ]
    name = models.TextField(choices=TYPE_COWORKING)
    price = models.FloatField(default=100.00)

    def __str__(self) -> str:
        return str(self.name)


class Place(models.Model):
    place_no = models.CharField(max_length=20, blank=False)
    type_place = models.ForeignKey(TypeCoworking, on_delete=models.CASCADE)
    is_prepared = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.place_no)


class Reservation(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Имя",
        default="Test"
    )
    phone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Номер телефона",
        default="Test"
    )
    email = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="E-mail"
    )
    comment = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="Комментарий"
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    checkin_date = models.DateField(default=datetime.date)

    def __unicode__(self):
        return self.id

    def save(self, **kwargs):
        super().save(**kwargs)

