# Generated by Django 3.2 on 2021-07-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nnc', '0002_auto_20210729_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Product', max_length=100),
            preserve_default=False,
        ),
    ]
