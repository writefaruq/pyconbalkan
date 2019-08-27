# Generated by Django 2.2.4 on 2019-08-27 11:59

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0014_sponsor_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='amount',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default_currency='EUR', max_digits=16),
        ),
    ]
