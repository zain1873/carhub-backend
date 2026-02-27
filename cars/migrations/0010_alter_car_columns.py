from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_car_likes_car_views'),  # last applied migration
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE cars_car
            ALTER COLUMN fuel_type TYPE varchar(50),
            ALTER COLUMN transmission TYPE varchar(50),
            ALTER COLUMN status TYPE varchar(50);
            """
        ),
    ]