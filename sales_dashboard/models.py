from django.db import models

# app_label = "sales_dashboard"
class SalesDay(models.Model):
    day = models.DateField(primary_key=True)
    sales = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "sales_2020Q4"
