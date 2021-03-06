# Generated by Django 3.2 on 2021-08-01 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nnc', '0003_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('total', models.IntegerField(default=0)),
                ('number_of_items', models.IntegerField(default=0)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('delivered', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nnc.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nnc.categoryproduct')),
            ],
        ),
    ]
