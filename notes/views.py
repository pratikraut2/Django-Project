from django.shortcuts import render 
from .models import Note

def home(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'notes/home.html', context)

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content)
    return render(request, 'notes/add.html')

def edit(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
    return render(request, 'notes/edit.html', {'note': note})

def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        note.delete()
    return render(request, 'notes/delete.html', {'note': note})

