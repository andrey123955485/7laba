from django.shortcuts import render, redirect
from .models import VisitCount

def home(request):
    # Проверяем, существует ли запись в базе данных
    visit_count, created = VisitCount.objects.get_or_create(id=1)
    # Увеличиваем счетчик
    visit_count.count += 1
    visit_count.save()

    return render(request, 'visits/home.html')

def monitoring(request):
    # Получаем текущее значение посещений
    visit_count = VisitCount.objects.get(id=1)
    return render(request, 'visits/monitoring.html', {'count': visit_count.count})
