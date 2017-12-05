from django.shortcuts import render

def index(request):
    dict = {'text': 'Hello World!', 'number': 100}
    return render(request, 'basic_app/index.html', context=dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

