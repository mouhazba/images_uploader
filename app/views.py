import re
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

# Create your views here.
def index(request, enctype="multipart/form-data"):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'app/index.html', context={'img': img,'form':form})


def delete(request, id_sup):
    response = Image.objects.get(id=id_sup).delete()
    return redirect(index)