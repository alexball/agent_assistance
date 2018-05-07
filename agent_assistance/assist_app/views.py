from django.shortcuts import render, redirect
from django.db.models import Count

from .models import Call

# Create your views here.

## Index of the app
## -----------------------------------------------------
def index(request):
    list_of_calls_needing_assistance = Call.objects.all()
    num_of_calls = Call.objects.filter(is_completed=False).count()
    context = {'list_of_calls_needing_assistance': list_of_calls_needing_assistance, 'count': num_of_calls}
    return render(request, 'assist_app/calls.html', context)


## Redirect the link to the site
## -----------------------------------------------------
def claim_call(request, call_id):
    # Retrieve the clicked call
    call_to_monitor = Call.objects.get(id=call_id)
    # Set databased is_claimed to true
    call_to_monitor.is_completed = True
    call_to_monitor.save()

    # Redirect the user to the url associated with action_item
    return redirect(call_to_monitor.purecloud_url)


## TO DO LIST
# Refactor the templates, clean it up to make it more usable
#    - Partially done. Could do more with the navigation and sidebar
# Convert the date/time and do subtraction. Want to know how long the call currently is as well as how long they've been asking for assistance.
# Figure out how to "add" calls to be monitored separately
# Figure out how to "add" calls direct from PureCloud
# Figure out refresh issue
