from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import InfoPage, Picture
from .forms import InfoForm, PhotoForm
from cloudinary.forms import cl_init_js_callbacks
import cloudinary.api
# Create your views here.

# landing page with picture carousel
def landing_view(request):
    queryset = Picture.objects.all() # list of objects
    context = {
        "object_list": queryset,
        "range": range(1, len(queryset))
    }
    return render(request, "landing.html", context)

# info page route, gets the needed information from database
def info_view(request):
    obj = InfoPage.objects.get(id=1)
    context = {
        "info": obj.info,
        "tel": obj.tel
    }
    return render(request, "info.html", context)

# update the information on info page
@login_required
def info_create(request):
    obj = InfoPage.objects.get(id=1) # needed object from database
    form = InfoForm(request.POST or None, instance=obj)
    queryset = Picture.objects.all()
    if form.is_valid():
        form.save()
        return redirect("../edit")
    context = {
        "form":form,
        "object_list":queryset
    }
    return render(request, "info_create.html", context)

# deletes carousel picture from database & cloudinary
@login_required
def delete_picture(request, my_id):
    obj = get_object_or_404(Picture, id=my_id)
    if request.method == "POST":
        cloudinary.api.delete_resources([obj.image])
        obj.delete()
        return redirect("/edit")
    context = {
        "object": obj
    }
    return render()

# uploads the picture to cloudinary
@login_required
def upload(request):
  context = dict( backend_form = PhotoForm())
  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()
        return redirect("../edit")
  return render(request, 'upload.html', context)
