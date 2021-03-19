# Generated by Django 3.1.7 on 2021-03-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=80, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
