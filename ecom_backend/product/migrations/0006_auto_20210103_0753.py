# Generated by Django 3.1.2 on 2021-01-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201209_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='productcomment',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]