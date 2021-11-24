from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import News, Category


# Create your views here.

def home(requests):
    news = News.objects.all()
    ctg = Category.objects.all()
    ctx = {
        "news": news,
        "ctgs": ctg
    }
    return render(requests, 'index.html', ctx)


def contact(requests):
    ctg = Category.objects.all()
    return render(requests, 'contact.html', {'ctgs':ctg})



def ctg(requests, slug):
    ctg_one = Category.objects.get(slug=slug)
    news = News.objects.all().filter(ctg_id=ctg_one.id)
    new = get_list_or_404(News)[-1]
    ctg = Category.objects.all()
    news1 = News.objects.all().filter(ctg_id=ctg_one.id).order_by('-id')
    print(new.photo.url)

    ctx = {
        "news": news,
        "ctgs": ctg,
        "ctg_one": ctg_one,
        "news1": news1,
        "new": new
    }
    return render(requests, 'category.html', ctx)

def view(requests, pk):
    new = News.objects.get(id=pk)
    ctg = Category.objects.all()

    ctx = {
        "new": new,
        "ctgs": ctg
    }
    return render(requests, 'view.html', ctx)

def search(requests):
    news = News.objects.all()
    if requests.GET:
        savol = requests.GET.get('v')
    else:
        savol = False
    yigilgan_news = []
    for i in news:
        if savol and (savol in i.title or savol in i.toliq_malumot):
            yigilgan_news.append(i)
    ctx = {
        "news": yigilgan_news
    }
    return render(requests, 'search.html', ctx)