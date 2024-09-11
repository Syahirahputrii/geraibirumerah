from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Jacket',
        'price': 'Rp 100.000,00',
        'description': 'Lengan panjang dan memiliki hoodie'
    }

    return render(request, "main.html", context)