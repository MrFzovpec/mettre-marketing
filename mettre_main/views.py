from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return render(request, 'general_pages/pages/index.html')
    else:
        return redirect('/signup')


def information(request):
    if request.user.is_authenticated:
        return render(request, 'general_pages/pages/information.html')
    else:
        return redirect('/signup')


def usage_description(request):
    if request.user.is_authenticated:
        return render(request, 'general_pages/pages/description.html')
    else:
        return redirect('/signup')


def marketing_analyze(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'general_pages/pages/marketing_analyze.html')
        else:
            text = request.POST['text']
            return render(request, 'general_pages/pages/marketing_analyze.html', {'text': text})
    else:
        return redirect('/signup')


def category_analyze(request):
    if request.user.is_authenticated:
        return render(request, 'general_pages/pages/category_analyze.html')
    else:
        return redirect('/signup')


def post_stat(request):
    if request.user.is_authenticated:
        return render(request, 'general_pages/pages/statistic.html')
    else:
        return redirect('/signup')
