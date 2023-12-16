from django.shortcuts import render, redirect
from .models import Mijoz


def index(request):
    if request.method == 'POST':
        ism = request.POST.get('ism', '')
        nomer = request.POST.get('nomer', '')
        email = request.POST.get('email','')
        if ism and nomer:
            mijoz = Mijoz(ism=ism, nomer=nomer)
            mijoz.save()

            return redirect('page', ism=ism, nomer=nomer)

    return render(request, 'index.html')


def yangi_sahifa(request, ism, nomer):
    # ism va nomer ma'lumotlarini olish
    context = {'ism': ism, 'nomer': nomer}
    return render(request, 'page.html', context)
from django.shortcuts import render
from django.views.generic import TemplateView

class PageRuView(TemplateView):
    template_name = 'pageru.html'
class PageUzView(TemplateView):
    template_name = 'pageuz.html'


# Create your views here.
