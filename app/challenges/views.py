from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month number")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {
            "text": challenge_text,
            "month": month,
            }
        return render(request, "challenges/challenge.html", context)
    except:
        raise Http404()