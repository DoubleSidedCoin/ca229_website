from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'StudentLifeApp/index.html')
   
def timetable(request):
    return render(request, 'StudentLifeApp/timetable.html')
    
def profile(request):
    return render(request, 'StudentLifeApp/profile.html')
    
def buildings(request):
    return render(request, 'StudentLifeApp/buildings.html')
    
def staff(request):
    return render(request, 'StudentLifeApp/staff.html')
    

