# Generated by Django 4.1 on 2023-05-31 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='главная'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='product.category'),
        ),
    ]
