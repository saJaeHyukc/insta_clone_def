# Generated by Django 4.1.1 on 2022-10-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intro',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]