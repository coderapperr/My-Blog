# Generated by Django 3.2.3 on 2021-05-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.CharField(max_length=1000),
        ),
    ]