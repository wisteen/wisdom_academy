from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'wisdom/home.html', {
        "hello":"Hello"
    })
     
def join(request):
         return render(request, 'wisdom/login.html', {
        "hello":"Hello"
    })
         
def register(request):
         return render(request, 'wisdom/register.html', {
        "hello":"Hello"
    })
         
def about(request):
         return render(request, 'wisdom/about.html', {
        "hello":"Hello"
    })
         
def contact(request):
         return render(request, 'wisdom/contact.html', {
        "hello":"Hello"
    })    
         
def course(request):
         return render(request, 'wisdom/course.html', {
        "hello":"Hello"
    })        