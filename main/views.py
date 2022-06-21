from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render
from main.models import Worker, Boss
from main import permissions
from rest_framework import viewsets, permissions
from rest_framework.decorators import APIView
from main.serializers import WorkerSerializer
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from main.permissions import IsOwnerOrReadOnly
from django.contrib import messages
from django.core.paginator import Paginator
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

class WorkerViewSet_detail(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]


class SearchWorker(APIView):
    def get(self,request, format=None, *args, **kwargs):
        w= Worker.objects.all()
        
        if request.path == 'worker/' + str(Worker.objects.get(name="Tom Edisson")) +'/':
            w = Worker.objects.filter(name = "Tom Edisson")
               
        else:
            pass
        serializer = WorkerSerializer(w, many =True)
        
        return JsonResponse(serializer.data, safe =False)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

def index(request):
    worker_list = Worker.objects.all()

    """  This is for the search bar without the datatableif 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(major__icontains=q)| Q(salary__icontains=q)| Q(work_Date__icontains=q)| Q(boss__icontains=q) )        
        worker_list = Worker.objects.filter(multiple_q)
    else:
         worker_list = Worker.objects.all()

        in index.html
        
        <div class="input-group mb-3">
          <form class = "form-inline my-2  my-lg-0">
          <input class="form-inline mr-sm-2" name = "q" type="search" placeholder="Search" aria-label="Recipient's username" aria-describedby="basic-addon2">
          <button class = "btn btn-outline-success my-2 my-sm-0" type = "submit">Search</button>
      </form>
        </div>
      
    """
    context = {
        'worker_list' : worker_list,
        'boss_list' : Boss.objects.all()
    }
    
    return render(request,'index.html', context)

def add_worker(request):
    if request.method =="POST":
        name = request.POST['name']
        major = request.POST['major']
        salary = request.POST['salary']
        boss_id = request.POST['boss']
        boss = Boss.objects.get(id=boss_id)
        work_date= request.POST['work_date']
        worker = Worker(name = name , major = major, salary=salary, boss=boss,work_date=work_date)
        worker.save()
        messages.info(request,'Worker added successfully')
    else:
        pass

    worker_list = Worker.objects.all()
    context = {
        'worker_list' : worker_list,
        'boss_list' : Boss.objects.all()
    }
    return render(request, 'add.html', context)

def delete_worker(request,myid):
    worker= Worker.objects.get(id=myid)
    worker.delete()
    messages.info(request, 'Worker deleted')
    return redirect('main:index')

def edit_worker(request,myid):
    sel_worker = Worker.objects.get(id = myid)
    worker_list = Worker.objects.all()
    
    context = {
        'sel_worker' : sel_worker,
        'worker_list': worker_list,
        'boss_list' : Boss.objects.all()
    }
    return render(request,'edit.html', context)

def update_worker(request,myid):
    worker = Worker.objects.get(id=myid)
    worker.name = request.POST['name']
    worker.major = request.POST['major']
    worker.salary = request.POST['salary']
    worker.work_date = request.POST['work_date']
    
    boss_id = request.POST['boss']
    worker.boss = Boss.objects.get(id=boss_id)
    
    worker.save()
    messages.info(request, "Updated!")
    return redirect('main:index')



def register(request):
    form=UserCreationForm
    if request.method == 'POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered.')
    return render(request,'registration/register.html',{'form':form})


