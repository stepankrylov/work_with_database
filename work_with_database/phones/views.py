from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    x = request.GET.get('sort')
    if x == 'name':
        phones = Phone.objects.all().order_by('name')
    elif x == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif x == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    context = {'phones_list': phones}
    return render(request, template, context)


def show_product(request, slu):
    template = 'product.html'
    prod = Phone.objects.get(slug=slu)
    context = {'prod': prod}
    return render(request, template, context)
