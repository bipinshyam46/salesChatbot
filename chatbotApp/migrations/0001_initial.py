# Generated by Django 4.1.5 on 2023-11-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=400)),
                ('availability_status', models.BooleanField(default=True)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]
