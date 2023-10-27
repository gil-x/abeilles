# Generated by Django 3.2 on 2021-09-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionGarden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question *')),
                ('response', models.TextField(verbose_name='Response *')),
                ('weight', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Questions pour le jardin',
                'verbose_name_plural': 'Questions pour le jardin',
                'ordering': ['weight', 'question'],
            },
        ),
        migrations.CreateModel(
            name='QuestionServicesInd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question *')),
                ('response', models.TextField(verbose_name='Response *')),
                ('weight', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Services particuliers',
                'verbose_name_plural': 'Services particuliers',
                'ordering': ['weight', 'question'],
            },
        ),
        migrations.CreateModel(
            name='QuestionServicesPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question *')),
                ('response', models.TextField(verbose_name='Response *')),
                ('weight', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Services pro',
                'verbose_name_plural': 'Services pro',
                'ordering': ['weight', 'question'],
            },
        ),
    ]
