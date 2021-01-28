from django.shortcuts import render
from .models import SalesDay


def sales_dashboard_view(request):
    days = SalesDay.objects.using("sales_db").all()
    return render(request, "sales_dashboard0.html", {"days": days})
