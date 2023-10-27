# Generated by Django 3.2 on 2021-10-12 11:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Nom')),
                ('target', models.CharField(choices=[('PARTICULIER', 'Particulier'), ('PROFESSIONNEL', 'Professionnel')], default='PARTICULIER', max_length=13, verbose_name='Service pour *')),
                ('weight', models.IntegerField(default=1, verbose_name='Poids de la catégorie')),
                ('title', models.CharField(max_length=50, verbose_name='Titre H1 de la page')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Nom')),
                ('available', models.BooleanField(default=False, verbose_name='Disponible')),
                ('description', models.TextField(blank=True, verbose_name='Descriptif du poste *')),
                ('amplitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Amplitude horaires *')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Lieu de travail *')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date de dépôt')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.category', verbose_name='Catégorie')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
