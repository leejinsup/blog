from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Article


from django.utils import timezone

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:15]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'blogs/index.html', context)

def register(request):
    ptitle = request.POST['title']
    pauthor = request.POST['author']
    pcontents = request.POST['contents']

    sql = Article(title=ptitle, author = pauthor, pub_date=timezone.now(), contents=pcontents)
    sql.save()

    return HttpResponseRedirect('../../blogs/')