# Generated by Django 4.0.1 on 2022-01-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0005_alter_me_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=150, verbose_name='مهارت')),
                ('done', models.BooleanField(default=True, verbose_name='تمام شده/نشده')),
            ],
        ),
    ]
