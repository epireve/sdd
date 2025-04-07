import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from PhoneReview.models import Brand, PhoneModel, Review

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Review.objects.all().delete()
        PhoneModel.objects.all().delete()
        Brand.objects.all().delete()
        
        # Create brands
        self.stdout.write('Creating brands...')
        brands = [
            {
                'name': 'Apple',
                'origin': 'United States',
                'manufacturing_since': 1976,
                'description': 'Apple Inc. is an American multinational technology company that designs, develops, and sells consumer electronics, computer software, and online services.',
                'website': 'https://www.apple.com'
            },
            {
                'name': 'Samsung',
                'origin': 'South Korea',
                'manufacturing_since': 1938,
                'description': 'Samsung Electronics is a multinational electronics company headquartered in Suwon, South Korea.',
                'website': 'https://www.samsung.com'
            },
            {
                'name': 'Google',
                'origin': 'United States',
                'manufacturing_since': 1998,
                'description': 'Google is an American multinational technology company focusing on search engine technology, online advertising, cloud computing, computer software, quantum computing, e-commerce, and artificial intelligence.',
                'website': 'https://www.google.com'
            },
            {
                'name': 'Xiaomi',
                'origin': 'China',
                'manufacturing_since': 2010,
                'description': 'Xiaomi Corporation is a Chinese designer and manufacturer of consumer electronics and related software, home appliances, and household items.',
                'website': 'https://www.mi.com'
            },
            {
                'name': 'OnePlus',
                'origin': 'China',
                'manufacturing_since': 2013,
                'description': 'OnePlus Technology is a Chinese consumer electronics manufacturer headquartered in Shenzhen, Guangdong.',
                'website': 'https://www.oneplus.com'
            }
        ]
        
        created_brands = []
        for brand_data in brands:
            brand = Brand.objects.create(**brand_data)
            created_brands.append(brand)
            self.stdout.write(f'Created brand: {brand.name}')
        
        # Create phone models
        self.stdout.write('Creating phone models...')
        phone_models = [
            # Apple phones
            {
                'brand': created_brands[0],
                'model_name': 'iPhone 15 Pro',
                'launch_date': date(2023, 9, 22),
                'platform': 'iOS',
                'os_version': 'iOS 17',
                'processor': 'A17 Pro',
                'ram': '8GB',
                'storage': '128GB, 256GB, 512GB, 1TB',
                'display': '6.1-inch Super Retina XDR',
                'camera': 'Triple 48MP, 12MP, 12MP',
                'battery': '3,274 mAh',
                'price': 999.00
            },
            {
                'brand': created_brands[0],
                'model_name': 'iPhone 14',
                'launch_date': date(2022, 9, 16),
                'platform': 'iOS',
                'os_version': 'iOS 16',
                'processor': 'A15 Bionic',
                'ram': '6GB',
                'storage': '128GB, 256GB, 512GB',
                'display': '6.1-inch Super Retina XDR',
                'camera': 'Dual 12MP, 12MP',
                'battery': '3,279 mAh',
                'price': 799.00
            },
            # Samsung phones
            {
                'brand': created_brands[1],
                'model_name': 'Galaxy S24 Ultra',
                'launch_date': date(2024, 1, 31),
                'platform': 'Android',
                'os_version': 'Android 14, One UI 6.1',
                'processor': 'Snapdragon 8 Gen 3',
                'ram': '12GB',
                'storage': '256GB, 512GB, 1TB',
                'display': '6.8-inch Dynamic AMOLED 2X',
                'camera': 'Quad 200MP, 12MP, 10MP, 50MP',
                'battery': '5,000 mAh',
                'price': 1199.99
            },
            {
                'brand': created_brands[1],
                'model_name': 'Galaxy Z Fold 5',
                'launch_date': date(2023, 8, 11),
                'platform': 'Android',
                'os_version': 'Android 13, One UI 5.1.1',
                'processor': 'Snapdragon 8 Gen 2',
                'ram': '12GB',
                'storage': '256GB, 512GB, 1TB',
                'display': '7.6-inch Dynamic AMOLED 2X (Main), 6.2-inch Dynamic AMOLED 2X (Cover)',
                'camera': 'Triple 50MP, 12MP, 10MP',
                'battery': '4,400 mAh',
                'price': 1799.99
            },
            # Google phones
            {
                'brand': created_brands[2],
                'model_name': 'Pixel 8 Pro',
                'launch_date': date(2023, 10, 12),
                'platform': 'Android',
                'os_version': 'Android 14',
                'processor': 'Google Tensor G3',
                'ram': '12GB',
                'storage': '128GB, 256GB, 512GB, 1TB',
                'display': '6.7-inch LTPO OLED',
                'camera': 'Triple 50MP, 48MP, 48MP',
                'battery': '5,050 mAh',
                'price': 999.00
            },
            {
                'brand': created_brands[2],
                'model_name': 'Pixel 7a',
                'launch_date': date(2023, 5, 10),
                'platform': 'Android',
                'os_version': 'Android 13',
                'processor': 'Google Tensor G2',
                'ram': '8GB',
                'storage': '128GB',
                'display': '6.1-inch OLED',
                'camera': 'Dual 64MP, 13MP',
                'battery': '4,385 mAh',
                'price': 499.00
            },
            # Xiaomi phones
            {
                'brand': created_brands[3],
                'model_name': 'Xiaomi 14 Ultra',
                'launch_date': date(2024, 2, 25),
                'platform': 'Android',
                'os_version': 'Android 14, MIUI 14',
                'processor': 'Snapdragon 8 Gen 3',
                'ram': '12GB, 16GB',
                'storage': '256GB, 512GB, 1TB',
                'display': '6.73-inch LTPO AMOLED',
                'camera': 'Quad 50MP, 50MP, 50MP, 50MP',
                'battery': '5,000 mAh',
                'price': 1299.99
            },
            {
                'brand': created_brands[3],
                'model_name': 'Redmi Note 13 Pro',
                'launch_date': date(2023, 9, 21),
                'platform': 'Android',
                'os_version': 'Android 13, MIUI 14',
                'processor': 'MediaTek Dimensity 7200',
                'ram': '8GB, 12GB',
                'storage': '128GB, 256GB, 512GB',
                'display': '6.67-inch AMOLED',
                'camera': 'Triple 200MP, 8MP, 2MP',
                'battery': '5,100 mAh',
                'price': 299.99
            },
            # OnePlus phones
            {
                'brand': created_brands[4],
                'model_name': 'OnePlus 12',
                'launch_date': date(2024, 1, 23),
                'platform': 'Android',
                'os_version': 'Android 14, OxygenOS 14',
                'processor': 'Snapdragon 8 Gen 3',
                'ram': '12GB, 16GB',
                'storage': '256GB, 512GB',
                'display': '6.82-inch LTPO AMOLED',
                'camera': 'Triple 50MP, 48MP, 64MP',
                'battery': '5,400 mAh',
                'price': 799.99
            },
            {
                'brand': created_brands[4],
                'model_name': 'OnePlus Nord 3',
                'launch_date': date(2023, 7, 12),
                'platform': 'Android',
                'os_version': 'Android 13, OxygenOS 13',
                'processor': 'MediaTek Dimensity 9000',
                'ram': '8GB, 16GB',
                'storage': '128GB, 256GB',
                'display': '6.74-inch AMOLED',
                'camera': 'Triple 50MP, 8MP, 2MP',
                'battery': '5,000 mAh',
                'price': 449.99
            }
        ]
        
        created_phone_models = []
        for model_data in phone_models:
            phone_model = PhoneModel.objects.create(**model_data)
            created_phone_models.append(phone_model)
            self.stdout.write(f'Created phone model: {phone_model.model_name}')
        
        # Create reviews
        self.stdout.write('Creating reviews...')
        reviews = [
            {
                'title': 'iPhone 15 Pro Review: A Worthy Upgrade',
                'content': 'The iPhone 15 Pro brings significant improvements over its predecessor. The A17 Pro chip delivers blazing performance, and the camera system produces stunning photos with excellent dynamic range. Battery life is solid, easily lasting a full day of heavy use.',
                'author': 'Tech Reviewer',
                'rating': 4.5,
                'pros': 'Powerful performance, Excellent camera system, Premium build quality',
                'cons': 'Still expensive, No major design changes, USB-C transition can be inconvenient for some users',
                'date_published': timezone.now() - timedelta(days=60),
                'external_link': 'https://example.com/reviews/iphone-15-pro'
            },
            {
                'title': 'Galaxy S24 Ultra: The Ultimate Android Flagship',
                'content': 'Samsung has refined its Ultra lineup with the S24 Ultra. The phone offers incredible performance, a versatile camera system, and a stunning display. The S Pen functionality continues to be a standout feature that no other flagship offers.',
                'author': 'Mobile Expert',
                'rating': 4.7,
                'pros': 'Exceptional display, Versatile camera system, Fantastic battery life, S Pen functionality',
                'cons': 'Expensive, Limited design changes from S23 Ultra, Large and heavy form factor',
                'date_published': timezone.now() - timedelta(days=30),
                'external_link': 'https://example.com/reviews/galaxy-s24-ultra'
            },
            {
                'title': 'Pixel 8 Pro: Google\'s Best Phone Yet',
                'content': 'The Pixel 8 Pro showcases the best of Google\'s hardware and software integration. The camera system is outstanding, capturing true-to-life colors and details. Google\'s AI features make the phone truly intelligent, and the clean Android experience is refreshing.',
                'author': 'Android Enthusiast',
                'rating': 4.6,
                'pros': 'Exceptional camera system, Clean Android experience, Powerful AI features',
                'cons': 'Battery life could be better, Slow charging compared to competitors',
                'date_published': timezone.now() - timedelta(days=90),
                'external_link': 'https://example.com/reviews/pixel-8-pro'
            },
            {
                'title': 'Xiaomi 14 Ultra: Camera Powerhouse',
                'content': 'The Xiaomi 14 Ultra delivers an incredible camera experience with its quad 50MP setup. The phone is blazing fast, has a gorgeous display, and offers exceptional battery life. MIUI has improved significantly but still has some quirks.',
                'author': 'Photography Expert',
                'rating': 4.4,
                'pros': 'Exceptional camera system, Bright and vivid display, Fast charging',
                'cons': 'Limited global availability, MIUI software can be polarizing',
                'date_published': timezone.now() - timedelta(days=15),
                'external_link': 'https://example.com/reviews/xiaomi-14-ultra'
            },
            {
                'title': 'OnePlus 12: Return to Form',
                'content': 'The OnePlus 12 represents a return to the company\'s roots, offering flagship specifications at a competitive price. The phone excels in performance, has a gorgeous display, and offers incredibly fast charging. OxygenOS remains one of the best Android skins.',
                'author': 'Value Seeker',
                'rating': 4.5,
                'pros': 'Excellent performance, Beautiful display, Ultra-fast charging, Competitive pricing',
                'cons': 'Camera still not quite flagship level, No official IP rating',
                'date_published': timezone.now() - timedelta(days=45),
                'external_link': 'https://example.com/reviews/oneplus-12'
            },
            {
                'title': 'iPhone 14 vs Pixel 7a: Mid-range Champions',
                'content': 'Comparing the iPhone 14 and Pixel 7a reveals two excellent mid-range options. The iPhone offers better overall performance and video capabilities, while the Pixel excels in still photography and pricing. Both offer excellent software support.',
                'author': 'Comparison Specialist',
                'rating': 4.3,
                'pros': 'Both offer excellent value, Good performance across both devices',
                'cons': 'iPhone is significantly more expensive, Pixel has slightly lower build quality',
                'date_published': timezone.now() - timedelta(days=75),
                'external_link': 'https://example.com/reviews/iphone-14-vs-pixel-7a'
            }
        ]
        
        for review_data in reviews:
            # Select 1 or 2 random phone models to associate with this review
            selected_models = random.sample(created_phone_models, random.randint(1, 2))
            
            # Save data without the models (which is a ManyToMany field)
            models_data = selected_models
            review = Review.objects.create(
                title=review_data['title'],
                content=review_data['content'],
                author=review_data['author'],
                rating=review_data['rating'],
                pros=review_data['pros'],
                cons=review_data['cons'],
                date_published=review_data['date_published'],
                external_link=review_data['external_link']
            )
            
            # Add the selected models to the review
            review.models.set(models_data)
            self.stdout.write(f'Created review: {review.title} for {", ".join([model.model_name for model in models_data])}')
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!')) 