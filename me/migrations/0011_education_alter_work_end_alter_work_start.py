# Generated by Django 4.0.1 on 2022-01-16 22:32

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0010_work_check_now'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=200, verbose_name='مقطع تحصیلی')),
                ('major', models.CharField(max_length=200, verbose_name='رشته درسی')),
                ('start', django_jalali.db.models.jDateField(verbose_name='تاریخ شروع')),
                ('check_now', models.BooleanField(default=False, verbose_name='تا الان')),
                ('end', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ پایان (اگر تا الان هست خالی بزار)')),
            ],
            options={
                'verbose_name': 'سابقه تحصیلی',
                'verbose_name_plural': 'سوابق تحصیلی',
            },
        ),
        migrations.AlterField(
            model_name='work',
            name='end',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ پایان همکاری(اگر تا الان هست خالی بزار)'),
        ),
        migrations.AlterField(
            model_name='work',
            name='start',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ شروع همکاری'),
        ),
    ]
