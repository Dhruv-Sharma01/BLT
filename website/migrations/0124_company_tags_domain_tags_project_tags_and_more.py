# Generated by Django 5.0.7 on 2024-08-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0123_tag_issue_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.tag"),
        ),
        migrations.AddField(
            model_name="domain",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.tag"),
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.tag"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.tag"),
        ),
        migrations.AlterField(
            model_name="issue",
            name="tags",
            field=models.ManyToManyField(blank=True, to="website.tag"),
        ),
    ]