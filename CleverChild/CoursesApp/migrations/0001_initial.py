# Generated by Django 4.0.5 on 2022-06-14 13:31

from django.conf import settings
import django.core.validators
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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.CharField(max_length=70)),
                ('category', models.CharField(choices=[('EE', 'Electrical Engineering'), ('CPE', 'Computer Engineering'), ('CS', 'Computer Science')], max_length=80)),
                ('video', models.URLField()),
                ('image', models.URLField()),
                ('summary', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoursesApp.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoursesApp.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
