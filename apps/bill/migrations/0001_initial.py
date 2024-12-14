# Generated by Django 5.1.3 on 2024-11-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_num', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('required_date', models.DateField()),
                ('status', models.CharField(choices=[('need approval', 'Need approval'), ('approve', 'Approve'), ('waiting Payment', 'Waiting Payment'), ('paid', 'Paid'), ('completed', 'Completed'), ('close', 'Close')], max_length=20)),
                ('ship_to', models.CharField(max_length=100)),
                ('bill_to', models.CharField(max_length=100)),
                ('total_net_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total_tax_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('doc_file', models.FileField(upload_to='documents/bills')),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('net_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tax_amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]