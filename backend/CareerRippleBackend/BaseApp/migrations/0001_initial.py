# Generated by Django 4.2.14 on 2024-07-28 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('posted_date', models.DateField()),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('lead', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('meeting_time', models.DateTimeField()),
                ('meeting_platform', models.CharField(max_length=100)),
                ('project_length', models.DurationField()),
                ('phase', models.IntegerField()),
                ('availability_per_week', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('project', models.ManyToManyField(to='BaseApp.project')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('mentorship', models.CharField(choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')], default='mentee', max_length=6)),
                ('timezone', models.DateTimeField(default=django.utils.timezone.now)),
                ('headline', models.CharField(max_length=250)),
                ('biography', models.TextField()),
                ('occupation', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('linkedin_link', models.URLField()),
                ('portfolio_link', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseApp.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseApp.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('user', models.ManyToManyField(to='BaseApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField(blank=True, null=True)),
                ('accomplishment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=150)),
                ('enter_year', models.DateField()),
                ('graduation_year', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseApp.userprofile')),
            ],
        ),
    ]
