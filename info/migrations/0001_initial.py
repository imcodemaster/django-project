# Generated by Django 3.1.7 on 2021-04-16 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacture', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('descriptions', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('sale', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]