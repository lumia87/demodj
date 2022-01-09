from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import contact_Form

# Create your views here.
def contact(request):
    context = {'cf':contact_Form}
    return render(request, 'contact/contact.html', context)

# Lấy dữ liệu từ form về db

def getContact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("save success")
    else:
        return HttpResponse('not POST')