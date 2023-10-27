# Generated by Django 3.2 on 2021-11-15 19:24

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentation', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Présentation générale')),
                ('services_presentation', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Présentation des services')),
                ('garden_presentation', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Présentation du jardin')),
                ('garden_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du jardin')),
                ('benefit1_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 1')),
                ('benefit1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 1')),
                ('benefit2_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 2')),
                ('benefit2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 2')),
                ('benefit3_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 3')),
                ('benefit3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 3')),
                ('benefit4_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 4')),
                ('benefit4', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 4')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
            ],
            options={
                'verbose_name': 'Accueil',
                'verbose_name_plural': '  Accueil',
            },
        ),
        migrations.CreateModel(
            name='PageAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
            ],
            options={
                'verbose_name': 'Qui somme-nous',
                'verbose_name_plural': ' AAE - Qui somme-nous',
            },
        ),
        migrations.CreateModel(
            name='PageBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('body_extra', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte `Vente directe`')),
                ('body_food', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte `fruits et légumes`')),
            ],
            options={
                'verbose_name': 'Jardin - paniers',
                'verbose_name_plural': 'Jardin - paniers',
            },
        ),
        migrations.CreateModel(
            name='PageCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('GARDEN', 'Jardin'), ('JOBHUNT', "Recherche d'emploi"), ('ASSOCIATION', 'Association'), ('SERVICES', 'Services'), ('SERVICES_PRO', 'Services aux Professionnels'), ('SERVICES_IND', 'Services Particuliers')], max_length=20, verbose_name='Role')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['role', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PageGarden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('testimony_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre de la section')),
                ('testimony1_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #1')),
                ('testimony1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #1')),
                ('testimony1_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #1')),
                ('testimony2_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #2')),
                ('testimony2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #2')),
                ('testimony2_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #2')),
                ('testimony3_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #3')),
                ('testimony3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #3')),
                ('testimony3_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #3')),
                ('benefit1_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 1')),
                ('benefit1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 1')),
                ('benefit2_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 2')),
                ('benefit2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 2')),
                ('benefit3_title', models.TextField(blank=True, null=True, verbose_name='Titre Avantage 3')),
                ('benefit3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Avantage 3')),
            ],
            options={
                'verbose_name': 'Jardin',
                'verbose_name_plural': 'Jardin',
            },
        ),
        migrations.CreateModel(
            name='PageGardenProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
            ],
            options={
                'verbose_name': 'Jardin - le projet',
                'verbose_name_plural': 'Jardin - le projet',
            },
        ),
        migrations.CreateModel(
            name='PageJobhunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('testimony_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre de la section')),
                ('testimony1_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #1')),
                ('testimony1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #1')),
                ('testimony1_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #1')),
                ('testimony2_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #2')),
                ('testimony2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #2')),
                ('testimony2_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #2')),
                ('testimony3_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #3')),
                ('testimony3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #3')),
                ('testimony3_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #3')),
                ('body_extra', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte `Comment postuler ?`')),
                ('image_extra', models.ImageField(blank=True, upload_to='', verbose_name='Image `Comment postuler ?`')),
            ],
            options={
                'verbose_name': "Demandeurs d'emploi",
                'verbose_name_plural': "Demandeurs d'emploi",
            },
        ),
        migrations.CreateModel(
            name='PageMissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
            ],
            options={
                'verbose_name': 'Missions, Valeurs, Engagement',
                'verbose_name_plural': 'AAE - Missions, Valeurs, Engagement',
            },
        ),
        migrations.CreateModel(
            name='PageServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('testimony_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre de la section')),
                ('testimony1_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #1')),
                ('testimony1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #1')),
                ('testimony1_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #1')),
                ('testimony2_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #2')),
                ('testimony2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #2')),
                ('testimony2_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #2')),
                ('testimony3_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #3')),
                ('testimony3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #3')),
                ('testimony3_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #3')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='PageServicesInd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('testimony_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre de la section')),
                ('testimony1_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #1')),
                ('testimony1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #1')),
                ('testimony1_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #1')),
                ('testimony2_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #2')),
                ('testimony2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #2')),
                ('testimony2_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #2')),
                ('testimony3_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #3')),
                ('testimony3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #3')),
                ('testimony3_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #3')),
            ],
            options={
                'verbose_name': 'Services pour particuliers',
                'verbose_name_plural': 'Services pour particuliers',
            },
        ),
        migrations.CreateModel(
            name='PageServicesPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
                ('testimony_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre de la section')),
                ('testimony1_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #1')),
                ('testimony1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #1')),
                ('testimony1_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #1')),
                ('testimony2_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #2')),
                ('testimony2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #2')),
                ('testimony2_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #2')),
                ('testimony3_image', models.ImageField(blank=True, upload_to='', verbose_name='Photo du client #3')),
                ('testimony3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du client #3')),
                ('testimony3_text', models.CharField(blank=True, max_length=512, null=True, verbose_name='Témoignage #3')),
            ],
            options={
                'verbose_name': 'Services pour professionnels',
                'verbose_name_plural': 'Services pour professionnels',
            },
        ),
        migrations.CreateModel(
            name='PageTerritorialInfluence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('headline', models.TextField(blank=True, null=True, verbose_name='Chapeau (H2)')),
                ('featured_image', models.ImageField(blank=True, upload_to='', verbose_name='Image en une')),
                ('body1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #1')),
                ('image1', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #1')),
                ('body2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #2')),
                ('image2', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #2')),
                ('body3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bloc de texte #3')),
                ('image3', models.ImageField(blank=True, upload_to='', verbose_name='Image optionnelle #3')),
                ('meta_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='META title')),
                ('meta_description', models.CharField(blank=True, max_length=140, null=True, verbose_name='META description')),
            ],
            options={
                'verbose_name': 'Rayonnement territorial',
                'verbose_name_plural': 'AAE - Rayonnement territorial',
            },
        ),
    ]