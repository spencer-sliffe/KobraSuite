# Generated by Django 5.1.4 on 2025-01-02 18:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['due_date']},
        ),
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='budgetcategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='debt',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='savingsgoal',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bill',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='budget',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='debt',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='savingsgoal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
