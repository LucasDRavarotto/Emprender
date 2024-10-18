from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CategoryForm, ContactoForm
from django.contrib import messages

from .forms import PostForm 


# Create your views here.

def home(request):
     # Verifica si hay un mensaje de éxito en la sesión
    if 'success_message' in request.session:
        success_message = request.session['success_message']
        del request.session['success_message']  # Elimina el mensaje después de usarlo
    else:
        success_message = None



    posts = Post.objects.all() #Obtenemos todos los posts
    context = {'posts': posts, 'success_message': success_message}
    return render(request, 'main.html', context)
    

#Creamos la vista de Contacto
def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Tu mensaje ha sido enviado exitosamente.')
            # Guarda el mensaje en la sesión para usarlo en la página principal
            request.session['success_message'] = '¡Gracias! Tu mensaje ha sido enviado exitosamente.'
            return redirect('home')  # Redirige a la página de inicio después de enviar el formulario
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})



def post_list(request, category_id):
    categoria = get_object_or_404(Category, id=category_id)
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


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = ContactoForm()  # Creamos la instancia del formulario

    # Procesamos el formulario si se envió
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Tu comentario ha sido enviado exitosamente.')
            return redirect('post_detail', post_id=post_id)  # Redirigir a la misma página
    
    # Renderizamos la plantilla con el post y el formulario
    return render(request, 'post/post_detail.html', {'post': post})


def buscar_posts(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(titulo__icontains=query) if query else Post.objects.all()
    
    return render(request, 'post/buscar_resultados.html', {'resultados': resultados, 'query': query})


