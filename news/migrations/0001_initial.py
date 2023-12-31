# Generated by Django 4.2 on 2023-05-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='news')),
                ('description', models.TextField()),
                ('news_text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('news_date', models.DateTimeField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
