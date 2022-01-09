from django.http.response import HttpResponse
from django.shortcuts import render
from .models import postForm

# Create your views here.
def blog(request):
    pF = postForm.objects.all()
    return render(request, 'blog/post.html', {'pF':pF})

def postDetail(request, id):
    pD=postForm.objects.get(id = id)
    return render(request, 'blog/postDetail.html', {'pD': pD})
    