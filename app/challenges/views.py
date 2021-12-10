from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk at least 20 minutes every day",
    "march": "Learn django at least 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may": "Eat no meat for the entire month",
    "june": "Eat no meat for the entire month",
    "july": "Eat no meat for the entire month",
    "august": "Eat no meat for the entire month",
    "september": "Eat no meat for the entire month",
    "october": "Eat no meat for the entire month",
    "november": "Eat no meat for the entire month",
    "december": "Eat no meat for the entire month"
}

def index(request):
    list_items = ""
    
    months = list(monthly_challenges.keys())
    for month in months:
        path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{path}\">{month.capitalize()}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month number")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)
    #return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("month not found")
