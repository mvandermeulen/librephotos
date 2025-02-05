# Generated by Django 4.2.16 on 2024-09-20 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "api",
            "0071_rename_person_label_probability_face_cluster_probability_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="face",
            name="person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="faces",
                to="api.person",
            ),
        ),
    ]
