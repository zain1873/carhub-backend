# cars/migrations/0012_fix_column_length.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        # Replace with your actual last migration file
        ('cars', '0010_alter_car_columns'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE cars_car
            ALTER COLUMN fuel_type TYPE varchar(50),
            ALTER COLUMN transmission TYPE varchar(50),
            ALTER COLUMN status TYPE varchar(50),
            ALTER COLUMN color TYPE varchar(30);
            """
        ),
    ]