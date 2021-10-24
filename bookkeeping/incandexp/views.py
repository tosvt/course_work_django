from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'incandexp/index.html')

def add_expense(request):
    return render(request, 'incandexp/add_expense.html')