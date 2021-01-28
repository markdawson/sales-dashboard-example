from django.shortcuts import render
from .models import SalesDay
import pandas as pd
import altair as alt


def sales_dashboard_view(request):
    days = SalesDay.objects.using("sales_db").filter()
    df = pd.DataFrame([[str(day.day), day.sales] for day in days],
                      columns=["day", "sales"])
    df['days'] = pd.to_datetime(df['day'])
    print(days)
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('day:T', title="Day", timeUnit="utcyearmonthdate"),
        y="sales",
        tooltip=["day:T", "sales"]
    ).properties(width=800)



    return render(request, "sales_dashboard.html", {"chart": chart.to_json()})
