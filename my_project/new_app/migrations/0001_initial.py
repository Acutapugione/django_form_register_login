# Generated by Django 5.0.2 on 2024-02-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StyleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.TextField(blank=True)),
                ('text_color', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
