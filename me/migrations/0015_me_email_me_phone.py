# Generated by Django 4.0.1 on 2022-01-16 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0014_rename_skill_skills_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='me',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره تلفن'),
        ),
    ]
