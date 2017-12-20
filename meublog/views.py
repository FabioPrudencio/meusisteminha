from django.shortcuts import render, redirect
from meublog.models import Post
from meublog.forms import PostForm

# Create your views here.
def home(request):
	title = 'maneiro'
	frase = 'qui bobagi'
	return render(request, 'meublog/index.html', {'titulo':title,'frase':frase})

def lista(request):
	lista = Post.objects.all().order_by('-id')
	return render(request, 'meublog/lista.html', {'lista_posts':lista})

def novo(request):
	form = PostForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(lista)
	return render(request, 'meublog/novo.html', {'form':form})

def atualiza(request, id):
	post = Post.objects.get(id=id)
	form = PostForm(request.POST or None, instance=post)

	if form.is_valid():
		form.save()
		return redirect(lista)
	return render(request, 'meublog/novo.html', {'form':form})

def exclui(request, id):
	post = Post.objects.get(id=id)
	post.delete()
	return redirect(lista)

