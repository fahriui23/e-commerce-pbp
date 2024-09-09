from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306212096',
        'name': 'Trias Fahri Naufal',
        'class': 'PBP B',

        'product': 'Beras Pandan Wangi',
        'price': '12000',
        'description': 'Beras Pandan Wangi adalah beras yang memiliki aroma pandan yang harum dan khas. Beras ini cocok untuk dijadikan nasi putih hangat yang lezat.',
    }

    return render(request, "main.html", context)
