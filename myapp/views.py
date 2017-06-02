from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .forms import ImageForm
from .models import Image


# from myapp.forms import ImageForm
# from myapp.models import Image

# Create your views here.



def index(request):
    saved = False
    # form = ImageForm(request.POST, request.FILES or None)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved = True
            return HttpResponseRedirect(reverse('image_list'))
        #     HttpResponseRedirect('/')
        # return render(request, 'index.html', {'form': form})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

    # form = ImageForm()
    # return render(request, "index.html", {'form': form})

def imageList(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})
