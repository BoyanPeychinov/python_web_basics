from django.shortcuts import render, redirect

from core.for_profile_funcs import get_profile, delete_profile_notes
from notes.note.models import Note
from notes.profiles.forms import CreateProfileForm


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


#
# def edit_profile(request, pk):
#     pass


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        return redirect('home page')
    else:
        delete_profile_notes(Note.objects.all())
        profile.delete()
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)
