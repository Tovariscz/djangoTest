from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Article, Comment

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	return render(request, 'index.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.object.get(id=article_id)
	except:
		raise Http404("Статья не найдена!")

	return render(request, 'detail.html', {'article': a})

def leave_comment(request, article_id):
	try:
		a = Article.object.get(id=article_id)
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(author_name - request.POST['name'], comment_text=request.POST['text'])

	return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))