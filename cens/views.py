from django.shortcuts import render

# Create your views here.
def cens(request):
    
    return render(request, "pages/cens.html", context={"title":"Secundario CENS"})