# Generated by Django 3.0.7 on 2020-07-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0007_recurringuserplan_card_masked_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planquota',
            name='value',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
