# Generated by Django 5.2.1 on 2025-06-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_schoolinfo_school_tricode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitcherstat',
            name='outs',
            field=models.IntegerField(),
        ),
    ]
