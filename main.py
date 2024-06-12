import requests,bs4,re

req = requests.get('https://www.jumia.co.ke/laptops/#catalog-listing')
req.raise_for_status()

passed_html = bs4.BeautifulSoup(req.text,'html.parser')
scraped_data = passed_html.select('h3.name')
filterd_data = []

ram_regex = re.compile(r"\b(\d+)\s?GB\s?RAM\b")

for products in scraped_data:
    mo = ram_regex.search(str(products))
    if mo:
        ram_value = int(mo.group(1))
        if ram_value >= 8:
            filterd_data.append(products)
            

print(filterd_data)


        


