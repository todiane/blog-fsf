# Generated by Django 3.2.20 on 2024-01-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_purpose', models.CharField(choices=[('', 'Reason for Contact'), ('Daily Availability', 'Daily Availability'), ('Hourly Availability', 'Hourly Availability'), ('Website Build', 'Website Build'), ('Order Enquiry', 'Order Enquiry'), ('Customer Service', 'Customer Service'), ('Feedback', 'Feedback'), ('Other', 'Other')], max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=44)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Messages from User',
                'ordering': ['-date_submitted'],
            },
        ),
    ]
