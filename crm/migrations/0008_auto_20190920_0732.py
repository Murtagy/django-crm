# Generated by Django 2.2.5 on 2019-09-20 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20190627_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'permissions': [('assign_organisation', 'Can assign organisation owner')]},
        ),
    ]
