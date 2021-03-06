# Generated by Django 4.0.1 on 2022-01-15 12:32

from django.db import migrations, models
import me.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=me.models.upload_image_path, verbose_name='عکس رزومه')),
                ('job', models.CharField(max_length=200, verbose_name='سمت شغلی')),
            ],
        ),
    ]
