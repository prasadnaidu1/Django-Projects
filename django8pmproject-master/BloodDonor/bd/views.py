from django.shortcuts import render
from django.views.generic import UpdateView

from .models import State
from .models import City
from .models import DonorRegister
from .models import OrigranizationRegister

def openDonorLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def openHomePage(request):
    type = "home"
    return render(request,"index.html",{"type":type})


def openOrganizationLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def openDonorRegister(request):
    type = request.GET.get("type")
    res = State.objects.values('name')
    states = ["State"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})


def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('idno').filter(name=sel_state)
    idno = 0
    for x in res:
        idno = x["idno"]
    res1 = City.objects.values('city_name').filter(state_name=idno)
    city_names = ["City"]
    if not res1:
        city_names = ["No City Available"]
    else:
        for x in res1:
            city_names.append(x['city_name'])

    res2 = State.objects.values('name')
    states = ["State"]
    for x in res2:
        states.append(x["name"])

    return render(request, "index.html", {"type": 'h_donor_register',"city_names":city_names,"states":sel_state,"key":"one"})


def registerDonor(request):
    d_name = request.POST.get('d_name')
    d_cno = request.POST.get('d_cno')
    d_state = request.POST.get('d_state')
    d_city = request.POST.get('d_city')
    d_email = request.POST.get('d_email')
    d_pass = request.POST.get('d_pass')

    res = City.objects.values('idno').filter(city_name=d_city)
    idno = 0
    for x in res:
        idno = x["idno"]

    dr = DonorRegister(name=d_name, contact_no=d_cno, city_name=City.objects.get(idno=idno), email_id=d_email,password=d_pass)
    dr.save()
    return render(request,"index.html",{"type":'h_donor',"message":"Registred"})


def donorlogin(request):
    global name,email
    username = request.POST.get("d_uname")
    password = request.POST.get("d_pass")

    res = DonorRegister.objects.filter(email_id=username,password=password)

    if not res:
        type = 'h_donor'
        return render(request, "index.html", {"type": type,"message":"Invalid User"})
    else:
        type = 'd_home'
        for x in res:
            name = x.name
            email = x.email_id
        print("-----",name,email)
        return render(request,"donorHome.html",{"type":type,"name":name,"email":email})


def opendonorhome(request):
    type = request.GET.get("type")
    name = request.GET.get("name")
    email = request.GET.get("email")
    return render(request,"donorHome.html",{"type":type,"name":name,"email":email})


def organization_login(request):
    username = request.POST.get("o_uname")
    password = request.POST.get("o_pass")

    res = OrigranizationRegister.objects.filter(email_id=username,password=password)

    if not res:
        type = 'h_organization'
        return render(request, "index.html", {"type": type,"message":"Invalid User"})
    else:
        type = 'o_home'
        name = ""
        for x in res:
            name = x.name
        return render(request,"organizationHome.html",{"type":type,"name":name})


def donorUpdate(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    city = request.POST.get("t3")
    password = request.POST.get("t4")
    email = request.POST.get("t5")

    print(email)
    return None


def donorUpdateProfile(request):
    type = request.GET.get("type")
    email = request.GET.get("email")

    result = DonorRegister.objects.filter(email_id=email)

    return render(request,"donorHome.html",{"type":type,"result":result})