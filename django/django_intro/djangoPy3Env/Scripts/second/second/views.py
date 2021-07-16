from django.http import HttpResponse
from django.shortcuts import render	# tenga en cuenta el import!
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)