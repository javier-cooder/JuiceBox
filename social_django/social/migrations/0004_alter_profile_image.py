# Generated by Django 3.2.5 on 2021-08-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20210728_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.png', upload_to=''),
        ),
    ]
