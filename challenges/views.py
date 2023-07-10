from django.shortcuts import render 
from django.template.loader import render_to_string 
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "One month without alcohol and soda",
    "february": "One month of being total Vegan",
    "march": "One month of sugar detox",
    "april": "One month of running 1 mile each day",
    "may": "One month of yoga every day",
    "june": "One month of social media detox",
    "july": "One month of caffeine detox",
    "august": "One month of eating only at home or home-cooked meal",
    "september": "One month of no Netflix and TV",
    "october": "One month of daily reading for at least 30 minutes",
    "november": "One month of daily mindfulness meditation for at least 20 minutes",
    "december": None
}
#"One month of doing a random act of kindness"
# Create your views here.

def index(request): #landing_page
    """list_items = ''
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f'<ul>{list_items}</ul>'"""

    months = monthly_challenges.keys()
    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_by_number(request, month): #redirecting
    months = list(monthly_challenges.keys())

    if(month > len(months)):
        #response_data = render_to_string('404.html')
        #return HttpResponseNotFound(response_data)
        raise Http404()
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    
    try:

        '''return HttpResponse(f'<h1 style="background-color:yellow; padding: 20px 10px; text-align:center">{challenge_text}</h1>') '''
        # return HttpResponse(render_to_string("challenges/challenge.html"))

        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name" : month
        })
    except:
        raise Http404()
    
    


    
