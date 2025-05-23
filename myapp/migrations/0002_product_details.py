# Generated by Django 5.2.1 on 2025-05-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('weight', models.IntegerField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='product/')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
