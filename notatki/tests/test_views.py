# notatki/tests/test_views.py

import pytest
from django.urls import reverse
from notatki.models import Notatka, Ulubione

@pytest.mark.django_db
def test_lista_notatek(client):
    Notatka.objects.create(tytul="TestTytul", tresc="TestTresc")
    response = client.get(reverse('lista_notatek'))
    assert response.status_code == 200
    assert "TestTytul" in str(response.content)

@pytest.mark.django_db
def test_dodaj_notatke(client):
    response = client.get(reverse('dodaj_notatke'))
    assert response.status_code == 200
    response_post = client.post(reverse('dodaj_notatke'), {'tytul': 'Nowa Notatka', 'tresc': 'Testowa treść'})
    assert response_post.status_code == 302
    assert Notatka.objects.count() == 1

@pytest.mark.django_db
def test_usun_notatke(client):
    notatka = Notatka.objects.create(tytul="TestTytul", tresc="TestTresc")
    response = client.post(reverse('usun_notatke', args=[notatka.id]))
    assert response.status_code == 302
    assert Notatka.objects.count() == 0

@pytest.mark.django_db
def test_notatka_szczegoly(client):
    notatka = Notatka.objects.create(tytul="TestTytul", tresc="TestTresc")
    response = client.get(reverse('notatka_szczegoly', args=[notatka.id]))
    assert response.status_code == 200
    assert "TestTytul" in str(response.content)

@pytest.mark.django_db
def test_dodaj_do_ulubionych(client):
    notatka = Notatka.objects.create(tytul="TestTytul", tresc="TestTresc")
    response = client.get(reverse('dodaj_do_ulubionych', args=[notatka.id]))
    assert response.status_code == 302
    assert Ulubione.objects.count() == 1

@pytest.mark.django_db
def test_usun_z_ulubionych(client):
    notatka = Notatka.objects.create(tytul="TestTytul", tresc="TestTresc")
    Ulubione.objects.create(notatka=notatka)
    response = client.get(reverse('usun_z_ulubionych', args=[notatka.id]))
    assert response.status_code == 302
    assert Ulubione.objects.count() == 0
