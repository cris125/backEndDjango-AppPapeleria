# Generated by Django 5.0 on 2023-12-15 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, related_name='papeleria_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='papeleria_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('value', models.DecimalField(decimal_places=3, max_digits=11)),
                ('existences', models.DecimalField(decimal_places=3, max_digits=11)),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='papeleria.user')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('registros', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='papeleria.registros')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='papeleria.user')),
            ],
        ),
    ]
