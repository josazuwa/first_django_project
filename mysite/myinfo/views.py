from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
    "Name" : "Jeffrey Osazuwa",
    "Track" : "Backend(Python)",
    "Message" : "You're doing a good job, but it is a little fast."
    }
    name = "My name is " + data["Name"] + "<br/>I am taking the  " + data["Track"] + " Track<br/> " + data["Message"]

    return HttpResponse(name)