from django.shortcuts import render


posts = [
	{
		'author' : 'Vishal',
		'title' : 'Blog Post 1',
		'content' : 'First Post Content',
		'date_published' : 'July 22, 2020'
	},
	{
		'author' : 'Mohan',
		'title' : 'Blog Post 2',
		'content' : 'Second Post Content',
		'date_published' : 'July 23, 2020'
	}

]


def home(request):
	context = { 
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})