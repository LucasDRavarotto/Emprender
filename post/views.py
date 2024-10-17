from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria
from .forms import CategoryForm

from .forms import PostForm 


# Create your views here.

def home(request):
    categorias = Categoria.objects.all() 
    context = {'categorias': categorias}
    return render(request, 'post/posts_page.html', context)   


def post_list(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    context={'posts': posts, 'categoria': categoria}
    return render(request, 'post/post.html',context)


def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form}
    return render (request , 'post/form_post.html', context)





    



