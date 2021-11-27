from django.shortcuts import render


# Create your views here.

def test(req):
    print('hello')
    return render(req, 'test.html')
