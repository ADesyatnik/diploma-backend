# Generated by Django 2.1.7 on 2020-06-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplomaBackend', '0004_action_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='name',
            field=models.CharField(default='qwert', max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
    ]