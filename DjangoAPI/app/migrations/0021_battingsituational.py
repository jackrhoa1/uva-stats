# Generated by Django 5.2.1 on 2025-06-16 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_pitcherstat_loss_alter_pitcherstat_starter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BattingSituational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.gameinfo')),
                ('player_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.playerinfo')),
            ],
        ),
    ]
