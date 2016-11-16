from django.shortcuts import render
from django.utils.translation import ugettext as _

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def portfolio(request):
    return render(request, 'home/portfolio.html', {
        'title': _('portfolio_meta_title'),
        'meta_description': _('portfolio_meta_description'),
    })

def about(request):
    return render(request, 'home/about.html', {
        'title': _('about_meta_title'),
        'meta_description': _('about_meta_description'),
    })
