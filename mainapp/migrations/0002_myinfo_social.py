# Generated by Django 4.1 on 2022-08-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('about1', models.TextField(blank=True, null=True)),
                ('about2', models.TextField(blank=True, null=True)),
                ('about3', models.TextField(blank=True, null=True)),
                ('address1', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta', models.TextField(blank=True, null=True)),
                ('facebook', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('linkedin', models.TextField(blank=True, null=True)),
                ('github', models.TextField(blank=True, null=True)),
                ('leetcode', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
