# Generated by Django 2.1.5 on 2019-02-18 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_book', '0006_auto_20190218_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_book.School'),
        ),
    ]
