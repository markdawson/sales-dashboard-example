from django.shortcuts import render
from .models import SalesDay
import pandas as pd
import altair as alt


def sales_dashboard_view(request):
    days = SalesDay.objects.using("sales_db").filter()
    df = pd.DataFrame([[str(day.day), day.sales] for day in days],
                      columns=["day", "sales"])
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('day:temporal', title="Day", timeUnit="utcyearmonthdate"),
        alt.Y("sales", title="Sales"),
        tooltip=[alt.Tooltip("day:temporal", title="Day", timeUnit="utcyearmonthdate"), alt.Tooltip("sales")]
    ).properties(width=800)

    return render(request, "sales_dashboard.html", {"chart": chart.to_json()})
