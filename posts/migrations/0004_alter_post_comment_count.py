# Generated by Django 4.0.2 on 2022-02-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
