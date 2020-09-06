# Generated by Django 2.2.13 on 2020-09-06 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('director', models.CharField(max_length=50)),
                ('actors', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('imdbname', models.CharField(max_length=20)),
                ('imdburl', models.CharField(max_length=100)),
                ('imageurl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=1000)),
                ('stars', models.IntegerField()),
                ('commenttime', models.CharField(max_length=20)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Film')),
            ],
            options={
                'ordering': ['commenttime'],
            },
        ),
    ]