from django.http import HttpResponse
from django.shortcuts import render

f = open(r'C:\Users\2004y\yash_project\django_app\mysite\mysite\one.txt', 'r')
content = f.read()

def index(request):
    return HttpResponse("Hello, yash")

def home(request):
    return HttpResponse(content)

def page1(request):
    return HttpResponse('''<h1>This the link</h1> <video controls muted>
    <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4"> </video> <br>

    <a href="https://www.youtube.com/watch?v=AepgWsROO4k">link 1 </a>
    ''')
def page2(request):
    return HttpResponse("Hello, user <a href='page1'>Back</a>")

def page3(request):
    doc = {"name":"yash", "place":"Mumbai","age":"18"}
    return render(request, "index.html", doc)