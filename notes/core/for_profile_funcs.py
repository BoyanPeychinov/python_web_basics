from notes.note.models import Note
from notes.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()

    if profile:
        profile.notes_count = Note.objects.count()

    return profile


def delete_profile_notes(notes):
    for note in notes:
        note.delete()
