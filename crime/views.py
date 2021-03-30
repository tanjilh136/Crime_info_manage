from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from . models import fileing
# Create your views here.
from .filters import CrimeFilter

def filee(request): 
    if request.method == 'POST':
        print('post method.............')
        cName = request.POST.get("cName")
        cRoad_Block_Sector = request.POST.get("cRoad_Block_Sector")
        cCity_Village_House = request.POST.get("cCity_Village_House")
        cPost_Office = request.POST.get("cPost_Office")
        cPostal_Code = request.POST.get("cPostal_Code")
        cDistrict = request.POST.get("cDistrict")
        cPolice_Station = request.POST.get("cPolice_Station")
        cCountry = request.POST.get("cCountry")
        Choose_Crime = request.POST.get("Choose_Crime")
        Time = request.POST.get("Time")
        Crime_Descrip = request.POST.get("Crime_Descrip")
        sName = request.POST.get("sName")
        sRoad_Block_Sector = request.POST.get("sRoad_Block_Sector")
        sCity_Village_House = request.POST.get("sCity_Village_House")
        sPost_Office = request.POST.get("sPost_Office")
        sPostal_Code = request.POST.get("sPostal_Code")
        sDistrict = request.POST.get("sDistrict")
        sPolice_Station = request.POST.get("sPolice_Station")
        sCountry = request.POST.get("sCountry")

        print(Crime_Descrip)
        print(type(Crime_Descrip))

        
        fileingg = fileing(cName=cName, cRoad_Block_Sector=cRoad_Block_Sector,cCity_Village_House=cCity_Village_House,
                    cPost_Office=cPost_Office,cPostal_Code=cPostal_Code, cDistrict=cDistrict,cPolice_Station=cPolice_Station,
                    cCountry=cCountry,Choose_Crime=Choose_Crime, Time=Time, Crime_Descrip=Crime_Descrip,sName=sName,
                    sRoad_Block_Sector=sRoad_Block_Sector,sCity_Village_House=sCity_Village_House,sPost_Office=sPost_Office,
                    sPostal_Code=sPostal_Code, sDistrict=sDistrict,sPolice_Station=sPolice_Station, sCountry=sCountry)
        
        fileingg.save()


    template_name= 'caseFiling2.html'
    return render(request, template_name)


def searchh(request):

    filee = fileing.objects.all() 


    myFilter = CrimeFilter(request.GET, queryset=filee)
    filee = myFilter.qs


    context= { 'myFilter': myFilter, 'filee': filee  }

    template_name= 'SearchCrime.html'
    return render(request, template_name, context)


def detail_page(request, id):
    obj = get_object_or_404(fileing, pk=id)


    return render(request, 'view_cases.html', {'obj':obj})




def src2(request):

    return render(request,'SearchAcrime.html')