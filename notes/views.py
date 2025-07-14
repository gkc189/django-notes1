from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.urls import reverse

# Create your views here.
from .models import Notes

def add_like_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.likes += 1
    note.save()
    return HttpResponseRedirect(reverse("notes.detail",args=(pk,)))

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

def list(request):
    all_notes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes':all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request,"notes/notes_detail.html",{"note":note})
