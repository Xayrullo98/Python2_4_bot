# Generated by Django 4.1.7 on 2023-03-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxsulot',
            name='tur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.menu'),
        ),
    ]