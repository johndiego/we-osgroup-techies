from django.http import HttpResponse
from .models import Meet,Speaker

def index(request):

    return HttpResponse("Hello, world. You're at the Meets Section.")


def details(request):
    meets=Meet.objects.order_by('meets_name')
    output = ', '.join([q.meets_name for q in meets])
    return HttpResponse(output)

