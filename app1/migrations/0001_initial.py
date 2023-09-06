# Generated by Django 4.2.3 on 2023-09-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'seller_tbl',
            },
        ),
        migrations.CreateModel(
            name='staff_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('designation', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'staff_tbl',
            },
        ),
        migrations.CreateModel(
            name='user_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'user_tbl',
            },
        ),
        migrations.CreateModel(
            name='useraccount_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('firstname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('accounttype', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'useraccount_tbl',
            },
        ),
    ]