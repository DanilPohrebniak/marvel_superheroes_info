# Generated by Django 4.1.7 on 2023-03-11 14:25

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
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='CATEGORY')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='TITLE')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='CONTENT')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='PHOTO')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='TIME CREATE')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='TIME UPDATE')),
                ('is_published', models.BooleanField(default=True, verbose_name='PUBLISHED')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marvel_heroes.category', verbose_name='CATEGORY')),
            ],
            options={
                'verbose_name': 'Main heroes',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]
