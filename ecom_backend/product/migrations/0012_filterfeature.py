# Generated by Django 3.1.2 on 2021-01-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210104_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20, verbose_name='Feature Key')),
                ('is_filter', models.BooleanField(default=False, verbose_name='Is Available For Filter')),
            ],
        ),
    ]
