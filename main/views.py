from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306212096',
        'name': 'Trias Fahri Naufal',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
