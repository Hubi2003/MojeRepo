# Generated by Django 4.2.5 on 2023-09-21 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notatki', '0002_kategoria_tag_komentarz_notatka_kategoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='komentarz',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='komentarz',
            name='notatka',
        ),
        migrations.RemoveField(
            model_name='notatka',
            name='kategoria',
        ),
        migrations.RemoveField(
            model_name='notatka',
            name='tagi',
        ),
        migrations.DeleteModel(
            name='Kategoria',
        ),
        migrations.DeleteModel(
            name='Komentarz',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]