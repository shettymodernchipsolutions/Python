from django.shortcuts import render
import datetime


# Create your views here.
# Good Morning Students,

# Welcome to Sandesh's Class

# Current Server Time:__________


def server_time(request):
    msg = '<h1>Welcome Client Good '

    # The below logic is to fetch the current server time
    server_time = datetime.datetime.now()

    # The below logic is to fetch the current server hour
    server_hour = int(datetime.datetime.now().hour)

    # The below logic is to display the appropriate greeting message for client a/c to server hour
    if server_hour > 0 and server_hour < 12:
        msg = 'Good Morning Students'

    elif server_hour > 12 and server_hour < 16:
        msg = 'Good Afternoon Students'

    elif server_hour > 16 and server_hour < 21:
        msg = 'Good Evening Students'

    else:
        msg = 'Good Night Students'

    my_msg = "Welcome to Sandesh's Class"

    data = msg + '\n' + my_msg

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='timeapp/time.html', context=dict)

