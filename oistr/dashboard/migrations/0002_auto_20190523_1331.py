# Generated by Django 2.2 on 2019-05-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='name',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='accepted',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='applied',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='contact',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='interview',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='offer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='rejected',
            field=models.CharField(default='', max_length=255),
        ),
    ]