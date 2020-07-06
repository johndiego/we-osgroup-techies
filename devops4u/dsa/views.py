from django.shortcuts import render
import logging 
from .models import Event

logger = logging.getLogger(__name__)

def index(request):

    data=Event.objects.all();

    event_details={"details":data}

    print(data)

    return render(request,'index.html',event_details)
