"""
urls.py
    urlpatterns = [
    path('', views.homepage),
    path('contact/', views.contact)
]

views.py
    from django.http import HttpResponse
    def homepage(request):
        return HttpResponse('<h1>This is a home page...</h1>')

    def contact(request):
        return HttpResponse('<h1>Contact page</h1><br>This is our contact page')
"""

"""
urls.py
    urlpatterns = [
    path('', views.homepage),
]

views.py
    from django.shortcuts import render
    def homepage(request):
        # return render(request, 'index.html')

        return render(request, 'index.html', {'name':'Hi there this is Abdul Zoha'})

settings.py
    'DIRS': ['templates'],

index.html
    <br>
    {{name}}
"""