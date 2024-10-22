from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# forzamos a que solo las personas legueadas puedan ir a esta url
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')