# Generated by Django 4.1 on 2022-08-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]