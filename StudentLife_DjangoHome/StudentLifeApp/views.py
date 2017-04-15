from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'StudentLifeApp/index.html')
   
def timetable(request):
    return HttpResponseRedirect('https://www.dcu.ie/registry/timetables.shtml#class')
    
def profile(request):
    return render(request, 'StudentLifeApp/profile.html')
    
def buildings(request):
    return render(request, 'StudentLifeApp/buildings.html')
    
def staff(request):
    return render(request, 'StudentLifeApp/staff.html')
    
def urlgen():
    default_dcu_tt = 'https://www101.dcu.ie/timetables/feed.php?prog=_&per=_&_&hour=1-28&template=student'
    
    default_dcu_tt = default_dcu_tt.split('_')
    
    sem1 = 'week1=1&week2=12'
    sem2 = 'week1=20&week2=31'
    
    if sem == '1':
        sem = sem1
    else:
        sem = sem2

    url = ''
    url = default_dcu_tt[0] + prog + default_dcu_tt[1] + year + default_dcu_tt[2] + sem + default_dcu_tt[3]
    return url
    

