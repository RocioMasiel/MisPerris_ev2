# Generated by Django 2.1.2 on 2018-10-28 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181028_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='status',
        ),
        migrations.AddField(
            model_name='perro',
            name='est',
            field=models.ForeignKey(default='DEFAULT VALUE', on_delete=django.db.models.deletion.CASCADE, to='core.Estado'),
        ),
    ]