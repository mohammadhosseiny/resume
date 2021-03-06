# Generated by Django 3.1.7 on 2021-03-19 11:00

from django.db import migrations, models
import portfolio_about.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection_Fa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(max_length=200, null=True, verbose_name='About Me')),
                ('about_me2', models.CharField(max_length=200, null=True, verbose_name='About Me 2')),
                ('image', models.ImageField(null=True, upload_to=portfolio_about.models.get_image_path, verbose_name='Image')),
                ('skill', models.CharField(max_length=130, verbose_name='My Primary Skills')),
                ('birthday', models.DateField(verbose_name='MY BirthDay')),
                ('website', models.URLField(blank=True, max_length=130, verbose_name='My Website')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('city', models.CharField(max_length=60, verbose_name='City')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('degree', models.CharField(max_length=60, verbose_name='Degree')),
                ('email', models.EmailField(max_length=60, verbose_name='Email')),
                ('freelance', models.BooleanField(default=False, verbose_name='Freelance :Available/unAvailable')),
            ],
        ),
    ]
