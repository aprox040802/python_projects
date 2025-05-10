from django.core.management.base import BaseCommand
from records.models import Record
from datetime import date, timedelta
import random
from django.db import connection

class Command(BaseCommand):
    help = 'Adds 100 sample records to the database'

    def handle(self, *args, **kwargs):
        # Clear existing records
        Record.objects.all().delete()
        
        # Reset the ID sequence to 1
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='records_record';")

        # Define products with their brands
        products = [
            ('Apple', ['iPhone 15 Pro', 'MacBook Pro', 'iPad Pro', 'AirPods Pro', 'Apple Watch Series 9']),
            ('Samsung', ['Galaxy S24 Ultra', 'Galaxy Z Fold 5', 'Galaxy Tab S9', 'Galaxy Buds Pro', 'Galaxy Watch 6']),
            ('Microsoft', ['Surface Laptop 5', 'Surface Pro 9', 'Surface Studio', 'Xbox Series X', 'Surface Headphones']),
            ('Dell', ['XPS 13', 'Alienware m16', 'Latitude 9440', 'Inspiron 16', 'Precision 5680']),
            ('HP', ['Spectre x360', 'Envy 16', 'Pavilion Plus', 'Omen 16', 'EliteBook 840']),
            ('Lenovo', ['ThinkPad X1 Carbon', 'Yoga 9i', 'Legion Pro 7', 'IdeaPad Pro 5', 'ThinkBook 16p']),
            ('ASUS', ['ROG Zephyrus G14', 'ZenBook Pro', 'TUF Gaming A16', 'ProArt StudioBook', 'VivoBook Pro']),
            ('Sony', ['WH-1000XM5', 'PlayStation 5', 'Alpha A7 IV', 'Xperia 1 V', 'WF-1000XM5']),
            ('LG', ['Gram 16', 'UltraGear 27GP950', 'DualUp Monitor', 'UltraWide 40WP95C', 'Gram Style']),
            ('Google', ['Pixel 8 Pro', 'Pixel Tablet', 'Pixel Watch 2', 'Pixel Buds Pro', 'Pixelbook Go'])
        ]

        descriptions = [
            'Latest model with cutting-edge technology',
            'Premium flagship device with top-tier features',
            'Professional-grade equipment for demanding users',
            'Innovative design with exceptional performance',
            'Best-in-class product with outstanding reviews',
            'High-performance device for power users',
            'Elegant design with premium build quality',
            'Feature-rich product with excellent value',
            'Industry-leading technology and innovation',
            'Award-winning product with superior quality'
        ]

        for i in range(100):
            brand, brand_products = random.choice(products)
            product = random.choice(brand_products)
            name = f"{brand} {product}"
            price = round(random.uniform(299, 2999), 2)
            quantity = random.randint(1, 50)
            date_of_entry = date.today() - timedelta(days=random.randint(0, 365))
            description = random.choice(descriptions)

            Record.objects.create(
                name=name,
                price=price,
                quantity=quantity,
                date_of_entry=date_of_entry,
                description=description
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 100 sample records with real brand names, starting from ID 1')) 