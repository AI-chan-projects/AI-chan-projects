from django.shortcuts import render

def main_page(request):
    return render(request, 'frontend/main_page.html')
