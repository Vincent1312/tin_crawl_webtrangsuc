import requests
from bs4 import BeautifulSoup
import time

import csv



#===================NOTE : VÌ WEB CỦ LÌN NÀY DÙNG CACHE CHO NÊN KHÔNG CÓ COOKIES NÓ LOAD HƠI LÂU TÍ, CHÈN COOKIES THÌ NÓ CRAWL NHANH HƠN :)


def main(category):
	cookies = {
		'_lscache_vary': 'd5c6a9ecd09a37a31c213c7eb6c0b64a',
		'sbjs_migrations': '1418474375998%3D1',
		'sbjs_current_add': 'fd%3D2024-06-25%2004%3A45%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fchat.zalo.me%2F',
		'sbjs_first_add': 'fd%3D2024-06-25%2004%3A45%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fchat.zalo.me%2F',
		'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dchat.zalo.me%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dchat.zalo.me%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36',
		'_gcl_au': '1.1.1923694580.1719290709',
		'_tt_enable_cookie': '1',
		'_ttp': 'fH1_1OdWOFt91RZfM2hxpTYZIYb',
		'_fbp': 'fb.1.1719290708892.596250715246386287',
		'_gid': 'GA1.2.1149701419.1719290709',
		'_ga': 'GA1.1.1214505514.1719290709',
		'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%3Fprice%3D%26min_price%3D0%26max_price%3D100000000%26orderby%3Dprice%26kieu_dang%3D',
		'cto_bundle': 'LSGZu19qN01zTEVXWENmQ2VicWtGdXZONkhkZVRncGlaY1FTVkgxMFJZb3pHVTE4Mk1tS1o1JTJGTmtEbU5kT0NhMWlmSlgyTVNXVEpmYlh3ZlJ0SElXJTJGRXY0RHV5MEdrVmZSTzJhV3I4cFdmZDdMcUZTJTJGOTBvcEtuVWxzck04eWdZRHd3d1l3UUhXSSUyQmI2cVN6aW9WbVlicERJZWpaNzNaUjJhQWlLSGNPR2szdG91byUzRA',
		'_ga_Z8XWJSJFB8': 'GS1.1.1719290708.1.1.1719290778.60.0.0',
		'_ga_5RK4CDGHY4': 'GS1.1.1719290709.1.1.1719290778.60.0.0',
	} 

	headers = {
		'accept': '*/*',
		'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		# 'cookie': '_lscache_vary=d5c6a9ecd09a37a31c213c7eb6c0b64a; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-25%2004%3A45%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fchat.zalo.me%2F; sbjs_first_add=fd%3D2024-06-25%2004%3A45%3A07%7C%7C%7Cep%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fchat.zalo.me%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dchat.zalo.me%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dchat.zalo.me%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1923694580.1719290709; _tt_enable_cookie=1; _ttp=fH1_1OdWOFt91RZfM2hxpTYZIYb; _fbp=fb.1.1719290708892.596250715246386287; _gid=GA1.2.1149701419.1719290709; _ga=GA1.1.1214505514.1719290709; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fkimngocthuy.com%2Fnhan-cuoi%2F%3Fprice%3D%26min_price%3D0%26max_price%3D100000000%26orderby%3Dprice%26kieu_dang%3D; cto_bundle=LSGZu19qN01zTEVXWENmQ2VicWtGdXZONkhkZVRncGlaY1FTVkgxMFJZb3pHVTE4Mk1tS1o1JTJGTmtEbU5kT0NhMWlmSlgyTVNXVEpmYlh3ZlJ0SElXJTJGRXY0RHV5MEdrVmZSTzJhV3I4cFdmZDdMcUZTJTJGOTBvcEtuVWxzck04eWdZRHd3d1l3UUhXSSUyQmI2cVN6aW9WbVlicERJZWpaNzNaUjJhQWlLSGNPR2szdG91byUzRA; _ga_Z8XWJSJFB8=GS1.1.1719290708.1.1.1719290778.60.0.0; _ga_5RK4CDGHY4=GS1.1.1719290709.1.1.1719290778.60.0.0',
		'priority': 'u=1, i',
		'referer': 'https://kimngocthuy.com/nhan-cuoi/page/4/?price&min_price=0&max_price=100000000&orderby=price&kieu_dang',
		'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
	}

	count = 1

	d = dict()
	with open(f'trangsuc_{category}.csv',newline='', mode='w', encoding="utf-8-sig") as file:
		fieldnames = ['product_name', 'sale_price', 'image_src','product_link']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader() #Viết header


		for page in range(1,100):


			response = requests.get(
				f'https://kimngocthuy.com/{category}/page/{page}/?price&min_price=0&max_price=100000000&orderby=price&kieu_dang',
				headers=headers,
				cookies=cookies
			)


			html_content = response.text

			soup = BeautifulSoup(html_content, 'html.parser')

			lst_data = []

			products = soup.find_all('li', class_='product')

			if products != []:

				# Loop through each product and extract name, price, and link...
				for product in products:
					# Extract product name
					name = product.find('h4').text.strip()

					# Extract product price
					price = product.find('span', class_='price').text.strip()

					# Extract product link
					link = product.find('a')['href']

					# Extract product image
					image_src = product.find('img')['src']

					# Print or process the extracted data as needed
					print(f"Sản phẩm thứ : {count} | Page {page}")
					print(f"Name: {name}")
					print(f"Price: {price}")
					print(f"Link: {link}")
					print(f"img: {image_src}")
					print("=" * 30)

					#APPEND TO EXCEL

					d['product_name'] = name
					d['sale_price'] = price
					d['image_src'] = link
					d['product_link'] = image_src
					writer.writerow(d) #Ghi giá trị

					count +=1

			
			else:
				print("HẾT SẢN PHẨM")
				print("Tự đóng file trong 5s")
				time.sleep(5)
				quit()

			time.sleep(1)

if __name__ == "__main__" : 
	category = "nhan-cuoi"
	main(category)
