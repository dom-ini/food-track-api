import datetime

from django.core import validators
from django.db import models
from django.utils import timezone


class DiaryEntry(models.Model):
    class Meta:
        verbose_name = "Diary entry"
        verbose_name_plural = "Diary entries"

    BREAKFAST = 0
    LUNCH = 1
    DINNER = 2
    SNACK = 3
    SUPPER = 4
    MEAL_CHOICES = (
        (BREAKFAST, "breakfast"),
        (LUNCH, "lunch"),
        (DINNER, "dinner"),
        (SNACK, "snack"),
        (SUPPER, "supper"),
    )
    user = models.ForeignKey(
        "auth.User",
        related_name="diary_entry",
        null=False,
        on_delete=models.CASCADE,
    )
    product_entry = models.ForeignKey(
        "diary.ProductEntry",
        related_name="diary_entry",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    meal = models.PositiveSmallIntegerField(
        choices=MEAL_CHOICES,
        null=False,
    )
    date = models.DateField(
        null=False,
    )
    created_at = models.DateTimeField(editable=False)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.date} - {self.product_entry}"


class ProductEntry(models.Model):
    class Meta:
        verbose_name = "Product entry"
        verbose_name_plural = "Product entries"

    product = models.ForeignKey("products.Product", related_name="product_entry", null=False, on_delete=models.CASCADE)
    weight = models.DecimalField(
        decimal_places=1,
        max_digits=6,
        null=False,
        default=0,
        validators=[
            validators.MinValueValidator(1, message="Waga musi być większa od 0"),
        ],
    )

    def __str__(self):
        return f"{self.product.name} - {self.weight} g"


class GoalsEntry(models.Model):
    class Meta:
        verbose_name = "Goals entry"
        verbose_name_plural = "Goals entries"

    user = models.ForeignKey("auth.User", related_name="goals_entry", null=False, on_delete=models.CASCADE)
    daily_kcal_goal = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
        ],
    )
    daily_protein_goal = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
            validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
        ],
    )
    daily_fat_goal = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
            validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
        ],
    )
    daily_carb_goal = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(1, message="Wartość musi być większa od 0"),
            validators.MaxValueValidator(100, message="Wartość może wynieść maksymalnie 100"),
        ],
    )
    from_date = models.DateField(null=False, blank=True, default=datetime.date.today)
    created_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Goals of user: {self.user} from day: {self.from_date}"
