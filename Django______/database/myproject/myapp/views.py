from django.shortcuts import render
from .models import Marks as db
from .models import *
from .values import *


def homepage(request):
    return render(request, "myapp/home.html")


def addstudent(request):
    if request.method == "POST":
        n = request.POST['name']
        r = request.POST['rollno']
        e = request.POST['english']
        k = request.POST['kannada']
        sc = request.POST['science']
        m = request.POST['maths']
        so = request.POST['social']
        h = request.POST['hindi']
        av = (int(e) + int(t) + int(sc) + int(m) + int(so) + int(h)) / 6
        if av >= 50:
            stat1 = 'Pass'
        else:
            stat1 = 'Fail'
        reg = Marks(Name=n, Roll_no=r, English=e, Tamil=k, Science=sc, Maths=m, Social=so, Hindi=h, Average=av,
                    Status=stat1)
        reg.save()
        result = "Student Mark Details are Saved"
        return render(request, 'myapp/home.html', {'res': result})
    else:
        result = "Student Mark Details are not Saved"
        return render(request, 'myapp/home.html', {'res': result})


def search(request):
    if request.method == "POST":
        n = request.POST['sn']
        try:
            sname = ''
            sroll = ''
            eng = ''
            tam = ''
            sci = ''
            mat = ''
            soc = ''
            hin = ''
            reg = Marks.objects.filter(Name=n)
            for i in reg:
                sname = sname + i.Name + ' '
                sroll = sroll + str(i.Roll_no) + ' '
                eng = eng + str(i.English) + ' '
                tam = tam + str(i.Tamil) + ' '
                sci = sci + str(i.Science) + ' '
                mat = mat + str(i.Maths) + ' '
                soc = soc + str(i.Social) + ' '
                hin = hin + str(i.Hindi) + ' '
            return render(request, 'myapp/retrieve.html',
                          {'r': "name=" + sname, 'r1': "rollno=" + sroll, 'r2': "english=" + eng, \
                           'r3': "tamil=" + tam, 'r4': "science=" + sci, 'r5': "maths=" + mat, \
                           'r6': "social=" + soc, 'r7': "hindi=" + hin})

        except:
            result = "Invalid Entry"
            return render(request, 'myapp/retrieve.html', {'r': result})

    else:
        return render(request, 'myapp/retrieve.html')


def update(request):
    if request.method == "POST":
        n = request.POST['sn']
        rrr = request.POST['rn']
        try:
            reg = Marks.objects.get(Name=n)
            reg.Roll_no = rrr
            reg.save()
            result = "Rollno Updated"
            return render(request, "myapp/update.html", {'r': result})
        except:
            result = "invalid"
            return render(request, "myapp/update.html", {'r': result})

    else:
        return render(request, "myapp/update.html")
