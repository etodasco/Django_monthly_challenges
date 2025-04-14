from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January: Eat no meat for the entire month!",
    "february": "February: Walk for at least 20 minutes every day!",
    "march": "March: Learn Django for at least 20 minutes every day!",
    "april": "April: Learn Django for at least 20 minutes every day!",
    "may": "May: Eat no meat for the entire month!",
    "june": "June: Walk for at least 20 minutes every day!",
    "july": "July: Learn Django for at least 20 minutes every day!",
    "august": "August: Learn Django for at least 20 minutes every day!",
    "september": "September: Eat no meat for the entire month!",
    "october": "October: Walk for at least 20 minutes every day!",
    "november": "November: Learn Django for at least 20 minutes every day!",
    "december": "December: Learn Django for at least 20 minutes every day!"
}

# Create your views here.


# def january(request):
#     return HttpResponse("January")

# def february(request):
#     return HttpResponse("February")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # challenge_text = None
    # if month == "january":
    #     challenge_text = "January"
    # elif month == "february":
    #     challenge_text = "February"
    # elif month == "march":
    #     challenge_text = "March"
    # elif month == "april":
    #     challenge_text = "April"
    # elif month == "may":
    #     challenge_text = "May"
    # elif month == "june":
    #     challenge_text = "June"
    # elif month == "july":
    #     challenge_text = "July"
    # elif month == "august":
    #     challenge_text = "August"
    # elif month == "september":
    #     challenge_text = "September"
    # elif month == "october":
    #     challenge_text = "October"
    # elif month == "november":
    #     challenge_text = "november"
    # elif month == "december":
    #     challenge_text = "December"
    # else:
    #     return HttpResponseNotFound("This is not a valid month!")
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
