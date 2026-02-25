import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'F10.settings')
django.setup()
from app1.models import Product, Category

# ── Categories ────────────────────────────────────────────────────────────────
electronics,  _ = Category.objects.get_or_create(name='Electronics',     slug='electronics')
accessories,  _ = Category.objects.get_or_create(name='Accessories',     slug='accessories')
fashion,      _ = Category.objects.get_or_create(name='Fashion',         slug='fashion')
home,         _ = Category.objects.get_or_create(name='Home & Kitchen',  slug='home-kitchen')
appliances,   _ = Category.objects.get_or_create(name='Appliances',      slug='appliances')
books,        _ = Category.objects.get_or_create(name='Books',           slug='books')
sports,       _ = Category.objects.get_or_create(name='Sports & Fitness',slug='sports-fitness')
beauty,       _ = Category.objects.get_or_create(name='Beauty & Health', slug='beauty-health')
toys,         _ = Category.objects.get_or_create(name='Toys & Games',    slug='toys-games')
automotive,   _ = Category.objects.get_or_create(name='Automotive',      slug='automotive')
# New
mobiles,      _ = Category.objects.get_or_create(name='Mobiles',         slug='mobiles')
mens_fashion, _ = Category.objects.get_or_create(name="Men's Fashion",   slug='mens-fashion')
womens_fashion,_= Category.objects.get_or_create(name="Women's Fashion", slug='womens-fashion')
kids_fashion, _ = Category.objects.get_or_create(name="Kids' Fashion",   slug='kids-fashion')

# ── Products ──────────────────────────────────────────────────────────────────
products_data = [

    # ── ELECTRONICS ────────────────────────────────────────────────────────────
    {'name':'Apple iPhone 17 Pro (256GB) - Desert Orange','slug':'iphone-17-pro-orange',
     'description':'A19 Pro chip, 48MP ProCamera, 5x optical zoom, titanium design, Desert Orange.',
     'price':134900.00,'image_url':'https://images.unsplash.com/photo-1695048292357-e9a4f25d9a1a?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'Apple MacBook Air M3 13.6-inch Liquid Retina','slug':'macbook-air-m3',
     'description':'8GB Unified Memory, 256GB SSD, all-day battery, fanless design, Midnight.',
     'price':104990.00,'image_url':'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'Sony WH-1000XM5 Noise Cancelling Headphones','slug':'sony-headphones-xm5',
     'description':'Industry-leading ANC, 30-hr battery, multipoint connect, LDAC.',
     'price':29990.00,'image_url':'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'Samsung 65-inch QLED 4K Smart TV (2024)','slug':'samsung-65-qled-tv',
     'description':'Quantum Dot Technology, Neo QLED 4K, Alexa built-in, 120Hz.',
     'price':99990.00,'image_url':'https://images.unsplash.com/photo-1593359677879-a4bb92f4834f?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'Dell XPS 15 Laptop (Core i7, 16GB, 512GB SSD)','slug':'dell-xps-15',
     'description':'15.6-inch OLED, NVIDIA RTX 4060, Windows 11 Pro.',
     'price':139990.00,'image_url':'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'iPad Air M2 (11-inch, 256GB, Wi-Fi)','slug':'ipad-air-m2',
     'description':'M2 chip, 12MP camera, USB-C, all-day battery, works with Apple Pencil Pro.',
     'price':74990.00,'image_url':'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&q=80&auto=format&fit=crop','category':electronics},
    {'name':'Canon EOS R10 Mirrorless Camera (18-45mm Kit)','slug':'canon-eos-r10',
     'description':'24.2MP APS-C sensor, 4K video, IBIS, fast AF with Animal/Eye detection.',
     'price':89990.00,'image_url':'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&q=80&auto=format&fit=crop','category':electronics},

    # ── MOBILES ────────────────────────────────────────────────────────────────
    {'name':'Apple iPhone 15 Pro (128GB) - Natural Titanium','slug':'iphone-15-pro',
     'description':'A17 Pro chip, Pro camera system, USB-C, Action button.',
     'price':127990.00,'image_url':'https://images.unsplash.com/photo-1603921326210-6edd2d60ca68?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Samsung Galaxy S24 Ultra 5G (12GB, 256GB, Titanium Gray)','slug':'samsung-s24-ultra',
     'description':'200MP camera, S Pen, Snapdragon 8 Gen 3, titanium frame.',
     'price':129999.00,'image_url':'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Google Pixel 8 Pro 5G (12GB, 256GB, Obsidian)','slug':'google-pixel-8-pro',
     'description':'Google Tensor G3, 50MP+48MP+48MP, 7-year OS guarantee.',
     'price':79999.00,'image_url':'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Realme 12 Pro+ 5G (8GB, 256GB, Navigator Beige)','slug':'realme-12-pro-plus',
     'description':'Snapdragon 7s Gen 2, 50MP Sony OIS camera, 67W fast charge.',
     'price':29999.00,'image_url':'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Motorola Edge 50 Pro 5G (12GB, 256GB, Luxe Lavender)','slug':'moto-edge-50-pro',
     'description':'Snapdragon 7 Gen 3, 50MP camera, 125W TurboPower, 1.5 months battery.',
     'price':31999.00,'image_url':'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Poco X6 Pro 5G (12GB, 256GB, Grey Mist)','slug':'poco-x6-pro',
     'description':'Dimensity 8300-Ultra, 64MP OIS camera, 67W fast charge, 120Hz.',
     'price':26999.00,'image_url':'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'Vivo V30 Pro 5G (12GB, 256GB, Peacock Green)','slug':'vivo-v30-pro',
     'description':'Snapdragon 7 Gen 3, Zeiss 50MP OIS camera, 80W FlashCharge.',
     'price':37999.00,'image_url':'https://images.unsplash.com/photo-1567581935884-3349723552ca?w=500&q=80&auto=format&fit=crop','category':mobiles},
    {'name':'iQOO Neo 9 Pro 5G (12GB, 256GB, Fighter Blue)','slug':'iqoo-neo-9-pro',
     'description':'Snapdragon 8 Gen 2, dual-cooled gaming mode, 144Hz, 120W charge.',
     'price':34999.00,'image_url':'https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=500&q=80&auto=format&fit=crop','category':mobiles},

    # ── ACCESSORIES ────────────────────────────────────────────────────────────
    {'name':'Apple AirPods Pro (2nd Gen) with MagSafe Case','slug':'airpods-pro-2',
     'description':'ANC, Transparency mode, Adaptive Audio, Spatial Audio.',
     'price':24900.00,'image_url':'https://images.unsplash.com/photo-1588423771073-b8903fead714?w=500&q=80&auto=format&fit=crop','category':accessories},
    {'name':'Anker 65W USB-C GaN Fast Charger','slug':'anker-65w-charger',
     'description':'Compact GaN, charges MacBook + iPhone + Android simultaneously.',
     'price':2499.00,'image_url':'https://images.unsplash.com/photo-1601999009162-2459b9f8278e?w=500&q=80&auto=format&fit=crop','category':accessories},
    {'name':'Logitech MX Master 3S Wireless Mouse','slug':'logitech-mx-master-3s',
     'description':'8K DPI, quiet clicks, MagSpeed scroll, USB-C quick charge.',
     'price':8995.00,'image_url':'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&q=80&auto=format&fit=crop','category':accessories},

    # ── MEN'S FASHION ──────────────────────────────────────────────────────────
    {'name':"Levi's 511 Slim Fit Jeans - Dark Wash",'slug':'levis-511-slim-jeans',
     'description':'Classic slim fit, stretch comfort waistband, dark indigo wash.',
     'price':2499.00,'image_url':'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"Van Heusen Men's Slim Fit Formal Shirt",'slug':'vh-formal-shirt',
     'description':'100% cotton, full-sleeve, wrinkle-resistant, office-ready.',
     'price':1299.00,'image_url':'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"Peter England Men's Regular Fit Chinos",'slug':'pe-chinos',
     'description':'Stretch fabric, flat-front, smart-casual, multiple colours.',
     'price':1799.00,'image_url':'https://images.unsplash.com/photo-1490114538077-0a7f8cb49891?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"Manyavar Men's Kurta Pyjama Set (Ethnic)",'slug':'manyavar-kurta',
     'description':'Premium silk blend, festive embroidery, straight fit kurta.',
     'price':3499.00,'image_url':'https://images.unsplash.com/photo-1583391733767-0b6f7bbff4a8?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':'Ray-Ban RB3025 Classic Aviator Sunglasses','slug':'rayban-aviator',
     'description':'Gold metal frame, G-15 green polarized lens, UV protection.',
     'price':8490.00,'image_url':'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"Nike Men's Revolution 7 Running Shoes",'slug':'nike-revolution-7',
     'description':'Breathable mesh upper, foam midsole, cushioned everyday run.',
     'price':3695.00,'image_url':'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"Woodland Men's Leather Nubuck Casual Shoes",'slug':'woodland-casual-shoes',
     'description':'Genuine nubuck leather, cushioned insole, anti-skid rubber sole.',
     'price':4799.00,'image_url':'https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=500&q=80&auto=format&fit=crop','category':mens_fashion},
    {'name':"The Indian Garage Co. Men's Striped Hoodie",'slug':'tig-hoodie',
     'description':'Fleece-lined, kangaroo pocket, adjustable drawstring, smart fit.',
     'price':1799.00,'image_url':'https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=500&q=80&auto=format&fit=crop','category':mens_fashion},

    # ── WOMEN'S FASHION ────────────────────────────────────────────────────────
    {'name':"Biba Women's Flared Anarkali Kurta Set",'slug':'biba-anarkali-kurta',
     'description':'Cotton blend, flared hem, printed dupatta, festive & casual.',
     'price':2499.00,'image_url':'https://images.unsplash.com/photo-1583391733956-62e3e6f8e3e7?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"W for Woman Printed Salwar Suit Set",'slug':'w-salwar-suit',
     'description':'Georgette fabric, printed tunic, palazzo pants, dupatta included.',
     'price':1999.00,'image_url':'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Libas Women's Pure Silk Saree with Blouse",'slug':'libas-silk-saree',
     'description':'Banarasi pure silk, zari border, vibrant weave, blouse piece.',
     'price':3999.00,'image_url':'https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Dressberry Women's Off-Shoulder Dress",'slug':'dressberry-dress',
     'description':'Ruffle hem, fitted waist, floral print, perfect for parties.',
     'price':1299.00,'image_url':'https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Lavie Women's Satchel Handbag (Tan)",'slug':'lavie-handbag',
     'description':'Faux leather, multiple compartments, detachable chain strap.',
     'price':2199.00,'image_url':'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Steve Madden Women's Block Heel Sandals",'slug':'steve-madden-heels',
     'description':'Padded ankle strap, 3-inch block heel, versatile nude finish.',
     'price':5499.00,'image_url':'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Tanishq Gold-Plated Jhumka Earrings",'slug':'tanishq-jhumka',
     'description':'22KT gold plating, kundan stone setting, traditional design.',
     'price':3999.00,'image_url':'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=500&q=80&auto=format&fit=crop','category':womens_fashion},
    {'name':"Allen Solly Women's Slim Fit Trousers",'slug':'allen-solly-women-trousers',
     'description':'Stretch ponte fabric, mid-rise waist, ankle-length, office wear.',
     'price':1499.00,'image_url':'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=500&q=80&auto=format&fit=crop','category':womens_fashion},

    # ── KIDS' FASHION ──────────────────────────────────────────────────────────
    {'name':"Max Kids Boys' Graphic T-shirt Combo (Pack of 3)",'slug':'max-boys-tshirt-combo',
     'description':'100% cotton, superhero prints, comfortable fit, ages 2-14.',
     'price':899.00,'image_url':'https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=500&q=80&auto=format&fit=crop','category':kids_fashion},
    {'name':"Hopscotch Girls' Floral A-Line Dress",'slug':'hopscotch-girls-dress',
     'description':'Cotton jersey, floral printed, knee length, elastic waist, ages 2-12.',
     'price':1199.00,'image_url':'https://images.unsplash.com/photo-1472162072942-cd5147eb3902?w=500&q=80&auto=format&fit=crop','category':kids_fashion},
    {'name':"Lotto Kids' Sports Running Shoes",'slug':'lotto-kids-shoes',
     'description':'Breathable mesh, lightweight EVA sole, Velcro closure, sizes 3-7.',
     'price':1299.00,'image_url':'https://images.unsplash.com/photo-1560243563-062bfc001d68?w=500&q=80&auto=format&fit=crop','category':kids_fashion},
    {'name':"Nauti Nati Girls' Ethnic Lehenga Choli Set",'slug':'nauti-nati-lehenga',
     'description':'Festive embroidered lehenga, crop choli, dupatta, ages 1-14.',
     'price':1799.00,'image_url':'https://images.unsplash.com/photo-1592188657297-c6473609e988?w=500&q=80&auto=format&fit=crop','category':kids_fashion},
    {'name':"Gini & Jony Boys' Cargo Shorts Set",'slug':'gini-jony-cargo-shorts',
     'description':'Twill fabric, multi-pocket cargo, drawstring waist, cool summer look.',
     'price':799.00,'image_url':'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=500&q=80&auto=format&fit=crop','category':kids_fashion},
    {'name':"UCB Kids' Polo T-Shirt (Combo of 2)",'slug':'ucb-kids-polo-combo',
     'description':'Pique cotton, ribbed collar, two contrasting colours, ages 4-12.',
     'price':1499.00,'image_url':'https://images.unsplash.com/photo-1465978313914-f66e5b38ddd5?w=500&q=80&auto=format&fit=crop','category':kids_fashion},

    # ── HOME & KITCHEN ─────────────────────────────────────────────────────────
    {'name':'Solimo Microfibre Reversible Comforter (Double)','slug':'solimo-comforter',
     'description':'Soft microfibre fill, machine washable, hypoallergenic, reversible.',
     'price':1299.00,'image_url':'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=500&q=80&auto=format&fit=crop','category':home},
    {'name':'Prestige Iris Plus 750W Mixer Grinder (4 Jars)','slug':'prestige-mixer',
     'description':'750W motor, 4 jars, ISI certified, overload protection.',
     'price':3299.00,'image_url':'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500&q=80&auto=format&fit=crop','category':home},
    {'name':'Pigeon 1.5L Electric Kettle (Auto Cut-Off)','slug':'pigeon-kettle',
     'description':'SS inner, boil-dry protection, cool-touch handle, fast boil.',
     'price':699.00,'image_url':'https://images.unsplash.com/photo-1544085311-11a028465b08?w=500&q=80&auto=format&fit=crop','category':home},
    {'name':'Sleepyhead 3-Layer Memory Foam Mattress (Queen)','slug':'sleepyhead-mattress',
     'description':'HR foam + memory foam, 100-night trial, 5-year warranty.',
     'price':11499.00,'image_url':'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&q=80&auto=format&fit=crop','category':home},
    {'name':'InstaCuppa French Press Coffee Maker (1L)','slug':'instacuppa-french-press',
     'description':'Borosilicate glass, 4-level filtration, stainless plunger.',
     'price':1299.00,'image_url':'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500&q=80&auto=format&fit=crop','category':home},
    {'name':'Non-Stick Cookware Set 3-piece Induction-Ready','slug':'cookware-set',
     'description':'PFOA-free aluminium, works on all stovetops incl. induction.',
     'price':1799.00,'image_url':'https://images.unsplash.com/photo-1556911073-52527ac43761?w=500&q=80&auto=format&fit=crop','category':home},

    # ── APPLIANCES ─────────────────────────────────────────────────────────────
    {'name':'Pigeon Healthifry Digital Air Fryer (4.2L)','slug':'pigeon-air-fryer',
     'description':'85% less oil, 8 preset modes, rapid-air technology.',
     'price':3499.00,'image_url':'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=500&q=80&auto=format&fit=crop','category':appliances},
    {'name':'Samsung 28L Convection Microwave Oven','slug':'samsung-microwave',
     'description':'Tandoor tech, ceramic enamel cavity, 900W power.',
     'price':11590.00,'image_url':'https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=500&q=80&auto=format&fit=crop','category':appliances},
    {'name':'LG 7.5 Kg 5-Star Smart Inverter Top-Load Washer','slug':'lg-washing-machine',
     'description':'TurboDrum, direct drive motor, 5-star BEE rating.',
     'price':17490.00,'image_url':'https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?w=500&q=80&auto=format&fit=crop','category':appliances},
    {'name':'Daikin 1.5 Ton 3-Star Inverter Split AC','slug':'daikin-ac',
     'description':'PM 2.5 filter, Econo mode, R-32 refrigerant, 5-year warranty.',
     'price':37990.00,'image_url':'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=500&q=80&auto=format&fit=crop','category':appliances},
    {'name':'Havells 250W Juicer Mixer Grinder (3 Jars)','slug':'havells-juicer',
     'description':'250W motor, 1.5L bowl, 3-speed + pulse, dishwasher-safe.',
     'price':2899.00,'image_url':'https://images.unsplash.com/photo-1600718374662-0483d2b9da44?w=500&q=80&auto=format&fit=crop','category':appliances},

    # ── BOOKS ──────────────────────────────────────────────────────────────────
    {'name':'Atomic Habits by James Clear','slug':'atomic-habits',
     'description':'Easy & proven way to build good habits and break bad ones.',
     'price':499.00,'image_url':'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&q=80&auto=format&fit=crop','category':books},
    {'name':'Rich Dad Poor Dad by Robert T. Kiyosaki','slug':'rich-dad-poor-dad',
     'description':'What the Rich Teach Their Kids About Money.',
     'price':299.00,'image_url':'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=500&q=80&auto=format&fit=crop','category':books},
    {'name':'The Alchemist by Paulo Coelho','slug':'the-alchemist',
     'description':'A story about following your dream and listening to your heart.',
     'price':199.00,'image_url':'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500&q=80&auto=format&fit=crop','category':books},
    {'name':'Wings of Fire by Dr. APJ Abdul Kalam','slug':'wings-of-fire',
     'description':"Autobiography of India's greatest scientist and President.",
     'price':249.00,'image_url':'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=500&q=80&auto=format&fit=crop','category':books},
    {'name':'Think and Grow Rich by Napoleon Hill','slug':'think-grow-rich',
     'description':'The definitive guide to achieving financial success and personal goals.',
     'price':249.00,'image_url':'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=500&q=80&auto=format&fit=crop','category':books},
    {'name':'The Psychology of Money by Morgan Housel','slug':'psychology-of-money',
     'description':'Timeless lessons on wealth, greed, and happiness.',
     'price':399.00,'image_url':'https://images.unsplash.com/photo-1553729459-efe14ef6055d?w=500&q=80&auto=format&fit=crop','category':books},

    # ── SPORTS ─────────────────────────────────────────────────────────────────
    {'name':'Boldfit Gym Duffel Bag (40L, Waterproof)','slug':'boldfit-gym-bag',
     'description':'Separate shoe compartment, adjustable strap, 40L capacity.',
     'price':899.00,'image_url':'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80&auto=format&fit=crop','category':sports},
    {'name':'Lifelong Resistance Bands Set (5 Levels)','slug':'lifelong-resistance-bands',
     'description':'Natural latex, anti-snap, for strength training and yoga.',
     'price':699.00,'image_url':'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=500&q=80&auto=format&fit=crop','category':sports},
    {'name':'Nivia Carbonite Web Football (Size 5)','slug':'nivia-football',
     'description':'Textured PU surface, hand-stitched, latex bladder.',
     'price':799.00,'image_url':'https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?w=500&q=80&auto=format&fit=crop','category':sports},
    {'name':'Cosco Yo-Yo Junior Cricket Kit','slug':'cosco-cricket-kit',
     'description':'Complete kit with bat, pads, gloves, helmet and bag.',
     'price':2499.00,'image_url':'https://images.unsplash.com/photo-1531415074968-036ba1b575da?w=500&q=80&auto=format&fit=crop','category':sports},
    {'name':'Decathlon Corded Skipping Rope','slug':'decathlon-skip-rope',
     'description':'Adjustable length, foam grip handles, smooth rotation bearing.',
     'price':349.00,'image_url':'https://images.unsplash.com/photo-1598971457999-ca4ef48a9a71?w=500&q=80&auto=format&fit=crop','category':sports},

    # ── BEAUTY & HEALTH ────────────────────────────────────────────────────────
    {'name':'Mamaearth Ubtan Face Wash (100ml)','slug':'mamaearth-ubtan-face-wash',
     'description':'Turmeric & saffron, toxin-free, for bright glowing skin.',
     'price':299.00,'image_url':'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=500&q=80&auto=format&fit=crop','category':beauty},
    {'name':'Minimalist 10% Vitamin C Face Serum (30ml)','slug':'minimalist-vitamin-c-serum',
     'description':'Brightens skin, reduces dark spots, stable L-ascorbic acid.',
     'price':599.00,'image_url':'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&q=80&auto=format&fit=crop','category':beauty},
    {'name':'Omron HEM-7120 Automatic BP Monitor','slug':'omron-bp-monitor',
     'description':'Clinically validated, 60-memory, irregular heartbeat indicator.',
     'price':1899.00,'image_url':'https://images.unsplash.com/photo-1559757175-5700dde675bc?w=500&q=80&auto=format&fit=crop','category':beauty},

    # ── TOYS ───────────────────────────────────────────────────────────────────
    {'name':'LEGO Classic Creative Bricks (900 Pieces)','slug':'lego-classic-creative',
     'description':'900 colourful bricks and baseplate – endless building fun.',
     'price':3999.00,'image_url':'https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=500&q=80&auto=format&fit=crop','category':toys},
    {'name':'Funskool Monopoly Classic Board Game','slug':'funskool-monopoly',
     'description':'Classic property trading for 2-8 players, ages 8+.',
     'price':745.00,'image_url':'https://images.unsplash.com/photo-1611891487122-207579d67d98?w=500&q=80&auto=format&fit=crop','category':toys},

    # ── AUTOMOTIVE ─────────────────────────────────────────────────────────────
    {'name':'Michelin Digital Tyre Inflator & Pressure Gauge','slug':'michelin-tyre-inflator',
     'description':'Digital display, inflate/deflate, LED torch, car 12V adapter.',
     'price':2199.00,'image_url':'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&q=80&auto=format&fit=crop','category':automotive},
    {'name':'GXIN 4K Front + 1080P Rear Dash Camera','slug':'gxin-dash-cam',
     'description':'Dual lens, night vision, parking monitor, G-sensor, 170° wide.',
     'price':3999.00,'image_url':'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=500&q=80&auto=format&fit=crop','category':automotive},
]

for p in products_data:
    obj, created = Product.objects.update_or_create(slug=p['slug'], defaults=p)
    print(f"  {'✅ Created' if created else '🔄 Updated'}: {p['name']}")

print(f"\n🎉 Done! {len(products_data)} products across all categories.")
