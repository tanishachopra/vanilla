# Generated by Django 2.0.6 on 2018-06-11 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'pledge',
                'verbose_name_plural': 'pledges',
            },
        ),
        migrations.CreateModel(
            name='User_Pledges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('datetime_taken', models.DateTimeField(auto_now_add=True, verbose_name='taken on')),
                ('pledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pledge.Pledge')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
