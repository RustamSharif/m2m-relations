# Generated by Django 5.0.7 on 2024-07-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scope',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]