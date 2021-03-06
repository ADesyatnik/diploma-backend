# Generated by Django 2.1.7 on 2020-06-02 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diplomaBackend', '0002_auto_20200603_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=250, verbose_name='Изображение')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='diplomaBackend.Company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AlterField(
            model_name='research',
            name='researcher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='researches', to='diplomaBackend.Employee', verbose_name='Работник'),
        ),
    ]
