import requests

def get_ip_info():
    # Fetch public IPv4 and IPv6 addresses and additional information
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()

        if response.status_code == 200:
            # Extracting information from the response
            ip_address = data.get("ip")
            ipv6_address = data.get("ip", "N/A")  # Depending on whether IPv6 is provided
            city = data.get("city")
            region = data.get("region")
            country = data.get("country_name")
            isp = data.get("org")
            asn = data.get("asn")
            country_code = data.get("country_code")
            latitude = data.get("latitude")
            longitude = data.get("longitude")

            # Formatting and displaying the IP information
            print("Public IP Information:")
            print(f"IP Address (IPv4/IPv6): {ip_address}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country} ({country_code})")
            print(f"ISP: {isp}")
            print(f"ASN: {asn}")
            print(f"Location: {latitude}, {longitude}")
        else:
            print(f"Failed to fetch IP information. Status Code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
get_ip_info()
