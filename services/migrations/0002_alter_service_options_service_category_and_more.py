# Generated by Django 5.0.6 on 2025-03-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(default='General', max_length=255),
        ),
        migrations.AddField(
            model_name='service',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
