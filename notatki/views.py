from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ulubione, Notatka
from .forms import NotatkaForm




def lista_notatek(request):
    notatki = Notatka.objects.all()
    ulubione = Ulubione.objects.all()
    ulubione_ids = [fav.notatka.id for fav in ulubione]
    return render(request, 'notatki/lista_notatek.html', {'notatki': notatki, 'ulubione_ids': ulubione_ids})


def dodaj_notatke(request):
    if request.method == "POST":
        form = NotatkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notatek')
    else:
        form = NotatkaForm()
    return render(request, 'notatki/dodaj_notatke.html', {'form': form})

def usun_notatke(request, notatka_id):
    notatka = get_object_or_404(Notatka, id=notatka_id)
    if request.method == "POST":
        notatka.delete()
        return redirect('lista_notatek')
    return render(request, 'notatki/usun_notatke.html', {'notatka': notatka})

def notatka_szczegoly(request, notatka_id):
    notatka = get_object_or_404(Notatka, id=notatka_id)
    return render(request, 'notatki/notatka_szczegoly.html', {'notatka': notatka})

from django.shortcuts import get_object_or_404, redirect

def dodaj_do_ulubionych(request, notatka_id):
    notatka = get_object_or_404(Notatka, id=notatka_id)
    Ulubione.objects.create(notatka=notatka)
    return redirect('lista_notatek')  # Powrót do listy notatek po dodaniu do ulubionych.

def lista_ulubionych(request):
    ulubione = Ulubione.objects.all()
    return render(request, 'notatki/lista_ulubionych.html', {'ulubione': ulubione})


def usun_z_ulubionych(request, notatka_id):
    # Spróbuj znaleźć notatkę w ulubionych
    try:
        ulubione = Ulubione.objects.get(notatka_id=notatka_id)
    except Ulubione.DoesNotExist:
        # Jeśli notatka nie jest w ulubionych, przekieruj z powrotem z odpowiednim komunikatem
        messages.error(request, "Notatka nie jest w ulubionych.")
        return redirect('lista_notatek')

    # Jeśli notatka jest w ulubionych, usuń ją
    ulubione.delete()
    messages.success(request, "Usunięto notatkę z ulubionych.")
    return redirect('lista_notatek')

