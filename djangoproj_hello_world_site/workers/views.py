from django.shortcuts import render
from workers.models import Worker

# Create your views here.

def workers_page(request):
    # new_worker = Worker(name='Пётр', second_name='Иванов', salary=50000)
    # new_worker.save()
    
    worker_to_change = Worker.objects.get(id=4) # достаём запись из базы по аттрибуту
    print(worker_to_change)
    worker_to_change.second_name = 'Шаманов' # меняем фамилию в записи
    worker_to_change.save() # сохраняем в базу
    print(worker_to_change)
    # Worker.objects.filter(id=4).update(second_name='Шаманов') # способ в одну строку

    all_workers = Worker.objects.all() # выбираем все объекты класса Worker
    print(all_workers)
    
    workers_filtered = Worker.objects.filter(salary=100000) # выбираем все записи класса Worker по аттрибуту
    print(workers_filtered)

    for i in all_workers:
        print(i.second_name, i.name, i.salary, i.id) # построчно выводим все записи
    return render(request, 'index.html')