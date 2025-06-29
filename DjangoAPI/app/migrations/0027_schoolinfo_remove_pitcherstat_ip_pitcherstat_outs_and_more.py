# Generated by Django 5.2.1 on 2025-06-22 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_rename_w_runners_battingsituational_bases_empty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=100, unique=True)),
                ('school_tricode', models.CharField(max_length=6, unique=True)),
                ('school_conference', models.CharField(max_length=5, null=True)),
                ('total_wins', models.IntegerField(null=True)),
                ('total_losses', models.IntegerField(null=True)),
                ('conference_wins', models.IntegerField(null=True)),
                ('conference_losses', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pitcherstat',
            name='ip',
        ),
        migrations.AddField(
            model_name='pitcherstat',
            name='outs',
            field=models.IntegerField(default=69),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='selected_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_team', to='app.schoolinfo'),
        ),
    ]
