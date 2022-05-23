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