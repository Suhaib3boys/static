# Generated by Django 3.2.12 on 2022-02-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_title', models.CharField(max_length=250)),
                ('why_text', models.TextField()),
                ('why_image', models.ImageField(upload_to='IMG')),
            ],
        ),
    ]
