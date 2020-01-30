# Generated by Django 3.0.2 on 2020-01-29 14:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="published_date",),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.TextField()),
                ("text", models.TextField()),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.Post"
                    ),
                ),
            ],
        ),
    ]
