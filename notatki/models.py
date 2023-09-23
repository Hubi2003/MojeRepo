from django.db import models

class Tag(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    tagi = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.tytul


class Ulubione(models.Model):
    notatka = models.ForeignKey(Notatka, on_delete=models.CASCADE)
    # Możesz dodać inne pola według potrzeb, na przykład:
    # data_dodania = models.DateTimeField(auto_now_add=True)


