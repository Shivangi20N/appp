# Generated by Django 3.0.5 on 2021-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]