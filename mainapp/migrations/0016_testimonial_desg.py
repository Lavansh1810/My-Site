# Generated by Django 4.1 on 2022-08-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='desg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
