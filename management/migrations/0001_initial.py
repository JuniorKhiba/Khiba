# Generated by Django 2.1.15 on 2022-01-11 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Phase')),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Project'),
        ),
    ]