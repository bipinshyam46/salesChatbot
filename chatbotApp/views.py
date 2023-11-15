from django.shortcuts import render
from .chatbot import question
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == "POST":
        messageInput = request.POST['messageInput']
        result = question(messageInput)
        context = {'messageInput':messageInput,'result':result}
        return render(request,'base.html',context)
        
    else:
        return render(request,'base.html')











