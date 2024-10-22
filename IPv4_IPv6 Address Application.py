pip install faker

from faker import Faker
import random

# Create a Faker instance
fake = Faker()

def generate_random_ip_info():
    # Randomly generate IP, geolocation, and network information
    ipv4 = fake.ipv4_public()
    ipv6 = fake.ipv6()
    city = fake.city()
    region = fake.state()
    country = fake.country()
    lat = round(random.uniform(-90.0, 90.0), 6)  # Random latitude
    lon = round(random.uniform(-180.0, 180.0), 6)  # Random longitude
    isp = fake.company()  # Random company as ISP
    asn = f"AS{random.randint(10000, 99999)}"  # Random ASN number

    # Print the generated information
    print("IP Address Information:")
    print(f"  IPv4 Address  : {ipv4}")
    print(f"  IPv6 Address  : {ipv6}")
    print(f"  City          : {city}")
    print(f"  Region        : {region}")
    print(f"  Country       : {country}")
    print(f"  Latitude      : {lat}")
    print(f"  Longitude     : {lon}")
    print(f"  ISP           : {isp}")
    print(f"  ASN           : {asn}")
    print("-" * 50)  # Separator between iterations

# Run the generator for 10 iterations
for i in range(10):
    print(f"Iteration {i + 1}:")
    generate_random_ip_info()
