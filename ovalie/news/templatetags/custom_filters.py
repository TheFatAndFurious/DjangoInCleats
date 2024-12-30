import datetime
from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def friendly_date(value):
    """Custom filter to display friendly dates."""
    now = timezone.now()
    if not isinstance(value, datetime.datetime):
        return value

    # Check if the day is today
    if value.date() == now.date():
        return f"{value.strftime('%Hh%M')}"

    # Check if the date is yesterday
    elif value.date() == (now - datetime.timedelta(days=1)).date():
        return f"Hier a {value.strftime('%Hh%M')}"

    #Default case: full date format with day
    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    months = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre",
              "Novembre", "Decembre"]
    day_name = days[value.weekday()]
    month_name = months[value.month - 1]

    return f"{day_name} {value.day} {month_name} a {value.strftime('%H:%M')}"
