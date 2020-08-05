from django.conf import settings
from django.db import models

class Book(models.Model):
    # auto_id is registration number
    class ClassChoices(models.TextChoices):
        PHILOSOPHY = ("100", "100 (Philosophy)")
        RELIGION = ("200", "200 (Religion)")
        SOCIAL_SCIENCE = ("300", "300 (Social Science)")
        LANGUAGE = ("400", "400 (Language)")
        PURE_SCIENCE = ("500", "500 (Pure Science)")
        APPLIED_SCIENCE = ("600", "600 (Applied Science)")
        ART = ("700", "700 (Art)")
        LITERATURE = ("800", "800 (Literature)")
        HISTORY = ("900", "900 (History)")

    class_number = models.CharField(max_length=4,
                                    choices=ClassChoices.choices)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    subject_keyword = models.CharField(max_length=40)
    issued_date = models.DateField()
    isbn = models.CharField(max_length=17)
    isOnload = models.BooleanField(default=False)
    reservation_number = models.IntegerField(default=0)




