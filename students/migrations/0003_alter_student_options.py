# Generated by Django 4.2.6 on 2023-10-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_modul'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'студент', 'verbose_name_plural': 'студенты'},
        ),
    ]