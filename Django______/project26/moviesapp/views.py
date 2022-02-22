from django.shortcuts import render
from moviesapp.models import MovieTable
from moviesapp.forms import MovieTableForm


# Create your views here.

def home_page(request):
    return render(request=request, template_name='moviesapp/homepage.html')


def add_movie(request):
    movie_form = MovieTableForm()

    # Logic to Store the data [POST request] entered by End user within the Database
    if request.method == 'POST':
        form_data = MovieTableForm(request.POST)
        if form_data.is_valid():
            form_data.save(commit=True)

    # Logic to fetch the data from the Form object and display the data on Django Development Server
    if request.method == 'POST':
        form_data = MovieTableForm(request.POST)
        if form_data.is_valid():

            print(f'MOVIE NAME:{form_data.cleaned_data["moviename"]}\n')
            print(f'HERO:{form_data.cleaned_data["hero"]}\n')
            print(f'HEROINE:{form_data.cleaned_data["heroine"]}\n')

    my_dict = {'movie_form': movie_form}
    return render(request=request, template_name='moviesapp/add.html', context=my_dict)


def movie_list(request):
    movie_data = MovieTable.objects.all()
    my_dict = {'movie_data': movie_data}
    return render(request=request, template_name='moviesapp/list.html', context=my_dict)
