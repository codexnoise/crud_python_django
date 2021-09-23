from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from mainapp.forms import FormArticle
from mainapp.models import Article
from django.contrib import messages
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'layout.html',{
        'title': 'Index Page',
    })

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {
                'articles': articles,
                'title': 'List Of Articles',
                })


def create_article(request):
    form = FormArticle(request.POST, request.FILES)
    if form.is_valid():
        data_form = form.cleaned_data
        title = data_form.get('title')
        content = data_form['content']
        image = data_form.get('image')
        articulo = Article(
            title = title,
            content = content,
            image = image
        )
        articulo.save()
        messages.success(request, f'{articulo.title} was created successfully')
        return redirect('articles')
    else:
        form = FormArticle()
        return render(request, 'create_article.html',{
                    'title': "Create Article",
                    'form':form
                    })

def clear_article(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    messages.warning(request, f"{articulo.title} was removed successfully")
    return redirect('articles')


def update_article(request, id):
    article = get_object_or_404(Article, pk=id)  
    if request.method == 'POST':      
        form = FormArticle(request.POST, request.FILES, instance=article)  
        if form.is_valid():
            article.save()
            return redirect('articles')
        else:
            form = FormArticle(instance=article) 
    else: 
        form = FormArticle(instance=article) 
        return render(request, 'create_article.html',{
                        'title': "Create Article",
                        'form': form
                        })