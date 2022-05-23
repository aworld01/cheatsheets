from django.shortcuts import render

def home(request):
    return render(request, "index.html")
def count(request):
    data = request.GET['textaria']
    word_list=data.split()
    n=len(word_list)
    return render(request, 'count.html', {'textaria':data, 'words':n})
