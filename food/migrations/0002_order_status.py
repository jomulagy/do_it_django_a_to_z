# Generated by Django 4.2.2 on 2023-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('none', 'none'), ('in_progress', 'in_progress'), ('done', 'done')], default='none', max_length=30),
        ),
    ]
