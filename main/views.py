from django.shortcuts import render
from main.models import Category, Portfolio, Contact
from main.forms import ContactForm 
from django.http import HttpResponse


def home(request):
    form = ContactForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> Biz bilan bog'langaniz uchun tashakkur! <h2>")
    else:
        categories = Category.objects.all()
        portfolios = Portfolio.objects.all()
        context = {
            'categories': categories,
            'portfolios': portfolios,
            'form':form,
        }
    return render(request, 'index.html', context)


def category(request):
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        'categories': categories,
        'portfolios': portfolios,
        'form':form,
        }
    return render(request, 'index.html', context)
