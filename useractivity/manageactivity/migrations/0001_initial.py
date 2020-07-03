# Generated by Django 3.0.5 on 2020-07-03 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=150, verbose_name='ID')),
                ('realName', models.CharField(max_length=150, verbose_name='RealName')),
                ('timeZone', models.CharField(max_length=150, verbose_name='TimeZone')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(verbose_name='StartTime')),
                ('endTime', models.DateTimeField(verbose_name='EndTime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageactivity.User')),
            ],
        ),
    ]