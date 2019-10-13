#coding=utf-8
from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime

#view

def homepage(request):
	posts = Post.objects.all()
	now = datetime.now()
	return render(request, 'index.html', locals())
	'''
	post_lists = list()
	for count, post in enumerate(posts):
		post_lists.append("No.{}".format(str(count)) + str(post) + "<br>")
		post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")
	return HttpResponse(post_lists)
	'''
def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
			return redirect('/')