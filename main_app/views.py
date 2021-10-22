from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Enclosure
from .forms import FeedingForm

class BirdCreate(CreateView):
  model = Bird
  fields = ['name', 'species', 'description', 'age']

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['species', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  # Get the enclosures the bird doesn't have
  enclosures_bird_doesnt_have = Enclosure.objects.exclude(id__in = bird.enclosures.all().values_list('id'))
  # Instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', {
    # Pass the bird and feeding_form as context
    'bird': bird, 'feeding_form': feeding_form,
    # Add the enclosures to be displayed
    'enclosures': enclosures_bird_doesnt_have
  })

def add_feeding(request, bird_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the bird_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)

def assoc_enclosure(request, bird_id, enclosure_id):
  Bird.objects.get(id=bird_id).enclosures.add(enclosure_id)
  return redirect('detail', bird_id=bird_id)

def unassoc_enclosure(request, bird_id, enclosure_id):
  Bird.objects.get(id=bird_id).enclosures.remove(enclosure_id)
  return redirect('detail', bird_id=bird_id)

class EnclosureList(ListView):
  model = Enclosure

class EnclosureDetail(DetailView):
  model = Enclosure

class EnclosureCreate(CreateView):
  model = Enclosure
  fields = '__all__'

class EnclosureUpdate(UpdateView):
  model = Enclosure
  fields = ['name', 'color']

class EnclosureDelete(DeleteView):
  model = Enclosure
  success_url = '/enclosures/'