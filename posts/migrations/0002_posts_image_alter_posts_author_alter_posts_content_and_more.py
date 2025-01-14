# Generated by Django 5.0.6 on 2024-06-20 08:03

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="image",
            field=models.FileField(
                blank=True, null=True, upload_to="Post Images", verbose_name="Şəkil"
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Yazıçı",
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="Məzmun"),
        ),
        migrations.AlterField(
            model_name="posts",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Başlıq"),
        ),
    ]
