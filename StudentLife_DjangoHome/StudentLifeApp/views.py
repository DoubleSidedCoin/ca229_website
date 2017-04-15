from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'StudentLifeApp/index.html')
   
def timetable(request):
    return render(request, 'StudentLifeApp/timetable.html')
    
def profile(request):
    return render(request, 'StudentLifeApp/profile.html')
    
