from django.shortcuts import render

# Create your views here.
def autorize(request):
    return render(request, 'User/index.html')