# Generated by Django 4.0.3 on 2022-04-07 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_book_borrower_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]