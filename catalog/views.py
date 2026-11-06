from django.http import HttpResponse, Http404

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1800},
    {"id": 2, "name": "Headphones", "price": 150},
    {"id": 3, "name": "Mouse", "price": 40},
]

def home(request):
    return HttpResponse('<h1>myshop</h1><br><a href="/products/">პროდუქტების სია</a>')

def about(request):
    return HttpResponse('გამარჯობა, მე ვსწავლობ Django-ს.')

def product_list(request):
    items = [f'<li><a href="/products/{p["id"]}/">{p["name"]}</a>: {p["price"]} ₾</li>' for p in PRODUCTS]
    return HttpResponse(f'<ul>{"".join(items)}</ul>')

def product_detail(request, pk):
    for p in PRODUCTS:
        if p["id"] == pk:
            return HttpResponse(f'{p["name"]}: {p["price"]} ₾')
    raise Http404("პროდუქტი ვერ მოიძებნა")