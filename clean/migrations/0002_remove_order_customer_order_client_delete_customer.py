# Generated by Django 4.2.7 on 2023-11-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
