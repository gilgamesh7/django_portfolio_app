# Generated by Django 2.2.1 on 2019-06-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190531_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]