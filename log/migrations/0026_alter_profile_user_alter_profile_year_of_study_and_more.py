# Generated by Django 4.2.5 on 2023-10-26 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0025_alter_registeration_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_of_study',
            field=models.CharField(choices=[('First year', 'First year'), ('Second year', 'Second year'), ('Third year', 'Third year'), ('Final year', 'Final year')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yugam_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
