from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def comnt(request, num):
    data={
        'num':num
    }
    return render(request, 'comnt.html', data)