# Generated by Django 3.1.7 on 2021-06-12 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_agent_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.userprofile'),
        ),
    ]
