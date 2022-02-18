from .models import Marks as db

def avg(var1):
    m1 = db.Marks.objects.get(Roll_no=var1)
    a = (m1.English + m1.Tamil + m1.Science + m1.Maths + m1.Social + m1.Hindi) / 6
    return a

def output():
    if avg() >= 50:
        return 'Pass'
    else:
        return 'Fail'

