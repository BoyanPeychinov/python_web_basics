from django.shortcuts import render, redirect

from petstagram_2.common.forms import CommentForm
from petstagram_2.common.models import Comment
from petstagram_2.pets.forms import CreatePetForm, EditPetForm
from petstagram_2.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
    }
    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()
    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == "POST":
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet list')
    else:
        form = CreatePetForm()

    context = {
        'form': form,
    }

    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet list')
    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('pet list')
    else:
        context = {
            'pet': pet,
        }
        return render(request, 'pets/pet_delete.html', context)


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
        )
        comment.save()

    return redirect('pet details', pk)

