# Generated by Django 4.1.1 on 2022-09-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_management', '0005_inbound_data_outbound_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material_stock',
            old_name='Uom',
            new_name='uom',
        ),
    ]