# Generated by Django 4.1.1 on 2022-09-09 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_management', '0006_rename_uom_material_stock_uom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inbound_data',
            old_name='vendor',
            new_name='serial_num',
        ),
        migrations.RenameField(
            model_name='outbound_data',
            old_name='customer',
            new_name='serial_num',
        ),
    ]
