import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Product , Brand

def seed_brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brands/{images[random.randint(0,11)]}"
        )

    print(f' {n} brands seeded successfully')



def seed_product(n):
    fake = Faker()
    images = ['01.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flag_type = ['New','Sale','Feature']
    for x in range(n):
        Product.objects.create(
            name = fake.name() , 
            price = round(random.uniform(20.99,99.99),2) , 
            quantity = random.randint(1,100) , 
            description = fake.text(max_nb_chars=3000),
            subtitle = fake.text(max_nb_chars=500),
            sku = random.randint(100,1000000) ,
            brand = Brand.objects.get(id=random.randint(1,102)),
            image = f"products/{images[random.randint(0,13)]}" , 
            flag = flag_type[random.randint(0,2)]
        )
    
    print(f' {n} products seeded successfully')


# seed_brand(100)
seed_product(3000)