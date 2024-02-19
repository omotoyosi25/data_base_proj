# Generated by Django 4.2.9 on 2024-01-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='blog title')),
                ('description', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveIntegerField()),
                ('published', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'post',
                'ordering': ['posted_at'],
            },
        ),
    ]