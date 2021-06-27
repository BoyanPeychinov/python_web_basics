from django.shortcuts import render, redirect
from core.for_profile_funcs import get_profile
from notes.note.forms import CreateNoteForm, DeleteNoteForm, EditNoteForm
from notes.note.models import Note


def home(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def create_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()
        context = {
            'form': form,
        }
        return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home page')
    else:
        form = DeleteNoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
        }
        return render(request, 'note-delete.html', context)


def show_note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)
