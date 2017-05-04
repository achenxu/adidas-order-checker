# adidasOrderChecker made by @therealchefuk

import requests
from bs4 import BeautifulSoup as bs

def getOrderDetailsUK(number, email):
	r = s.get("https://www.adidas.co.uk/order-tracker", headers=headers)
	soup = bs(r.content, "html.parser")
	url = soup.find('form', {'id': 'dwfrm_ordersignup'})['action']
	data = {'dwfrm_ordersignup_orderNo': number,
	'dwfrm_ordersignup_email': email,
	'dwfrm_ordersignup_signup': 'VIEW ORDER'}
	r = s.post(url, data=data, headers=headers)
	soup = bs(r.content, "html.parser")
	try:
		items = soup.find_all('div', {'class': 'order-step selected'})
		for item in items:
			status = item.find('div', {'class': 'order-step-content-wrp'})
			status = (status.text).strip()
		if str(status) == "Order confirmed, waiting to be packed":
			print("Order {} for {} is confirmed and waiting to be packed".format(number, email))
			confirmed_orders.append(number)
		elif "Shipped" in str(status):
			print("Order {} for {} has been shipped and is on its way to you!".format(number, email))
			shipped_orders.append(number)
			confirmed_orders.append(number)
		elif str(status) == "Preparing shipment":
			print("Order {} for {} is being prepared for shipping".format(number, email))
			confirmed_orders.append(number)
		elif str(status) == "Order processing":
			print("Order {} for {} has not been confirmed yet and is still processing".format(number, email))
	except:
		print("Order {} for {} has not shipped or is an invalid input".format(number, email))

def getOrderDetailsFR(number, email):
	r = s.get("https://www.adidas.fr/suivi-commande", headers=headers)
	soup = bs(r.content, "html.parser")
	url = soup.find('form', {'id': 'dwfrm_ordersignup'})['action']
	data = {'dwfrm_ordersignup_orderNo': number,
	'dwfrm_ordersignup_email': email,
	'dwfrm_ordersignup_signup': 'VOIR MA COMMANDE'}
	r = s.post(url, data=data, headers=headers)
	soup = bs(r.content, "html.parser")
	try:
		items = soup.find_all('div', {'class': 'order-step selected'})
		for item in items:
			status = item.find('div', {'class': 'order-step-content-wrp'})
			status = (status.text).strip()
		if str(status) == "Commande confirmée, en attente d'être préparée":
			print("Order {} for {} is confirmed and waiting to be packed".format(number, email))
			confirmed_orders.append(number)
		elif "Expédiée" in str(status):
			print("Order {} for {} has been shipped and is on its way to you!".format(number, email))
			shipped_orders.append(number)
			confirmed_orders.append(number)
		elif str(status) == "Expédition en cours de préparation":
			print("Order {} for {} is being prepared for shipping".format(number, email))
			confirmed_orders.append(number)
		elif str(status) == "Commande en cours de traitement":
			print("Order {} for {} has not been confirmed yet and is still processing".format(number, email))
	except:
		print("Order {} for {} has not shipped or is an invalid input".format(number, email))

def getOrderDetailsDE(number, email):
	r = s.get("https://www.adidas.de/bestellverfolgung", headers=headers)
	soup = bs(r.content, "html.parser")
	url = soup.find('form', {'id': 'dwfrm_ordersignup'})['action']
	data = {'dwfrm_ordersignup_orderNo': number,
	'dwfrm_ordersignup_email': email,
	'dwfrm_ordersignup_signup': 'BESTELLUNG ANSEHEN'}
	r = s.post(url, data=data, headers=headers)
	soup = bs(r.content, "html.parser")
	try:
		items = soup.find_all('div', {'class': 'order-step selected'})
		for item in items:
			status = item.find('div', {'class': 'order-step-content-wrp'})
			status = (status.text).strip()
		if str(status) == "Bestellung bestätigt, wird bald verpackt":
			print("Order {} for {} is confirmed and waiting to be packed".format(number, email))
			confirmed_orders.append(number)
		elif "Verschickt" in str(status):
			print("Order {} for {} has been shipped and is on its way to you!".format(number, email))
			shipped_orders.append(number)
			confirmed_orders.append(number)
		elif str(status) == "Der Versand wird vorbereitet":
			print("Order {} for {} is being prepared for shipping".format(number, email))
			confirmed_orders.append(number)
		elif str(status) == "Bestellung wird bearbeitet":
			print("Order {} for {} has not been confirmed yet and is still processing".format(number, email))
	except:
		print("Order {} for {} has not shipped or is an invalid input".format(number, email))

def getOrderDetailsUS(number, email):
	r = s.get("https://www.adidas.com/us/order-tracker", headers=headers)
	soup = bs(r.content, "html.parser")
	url = soup.find('form', {'id': 'dwfrm_ordersignup'})['action']
	data = {'dwfrm_ordersignup_orderNo': number,
	'dwfrm_ordersignup_email': email,
	'dwfrm_ordersignup_signup': 'Track order'}
	r = s.post(url, data=data, headers=headers)
	soup = bs(r.content, "html.parser")
	try:
		items = soup.find_all('div', {'class': 'order-step selected'})
		for item in items:
			status = item.find('div', {'class': 'order-step-content-wrp'})
			status = (status.text).strip()
		if str(status) == "Order confirmed, waiting to be packed":
			print("Order {} for {} is confirmed and waiting to be packed".format(number, email))
			confirmed_orders.append(number)
		elif str(status) == "Order processing":
			print("Order {} for {} has not been confirmed yet and is still processing".format(number, email))
		elif "Shipped" in str(status):
			print("Order {} for {} has been shipped and is on its way to you!".format(number, email))
			shipped_orders.append(number)
			confirmed_orders.append(number)
		elif str(status) == "Preparing shipment":
			print("Order {} for {} is being prepared for shipping".format(number, email))
			confirmed_orders.append(number)
	except:
		print("Order {} for {} is an invalid input".format(number, email))



s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Origin': 'http://www.adidas.co.uk'}
locale = input("LOCALE (US/UK/DE/FR):	")
confirmed_orders = []
shipped_orders = []
f = open("orders.txt", "r")
for item in f.read().splitlines():
	if not item == '':
		parts = item.split(":")
		if locale.upper() == "UK":
			getOrderDetailsUK(parts[0], parts[1])
		elif locale.upper() == "DE":
			getOrderDetailsDE(parts[0], parts[1])
		elif locale.upper() == "FR":
			getOrderDetailsFR(parts[0], parts[1])
		else:
			getOrderDetailsUS(parts[0], parts[1])
f.close()
count = len(confirmed_orders)
if count > 5:
	print("\nYou have {} confirmed orders, coooook!".format(count))
else:
	print("\nYou have {} confirmed orders!".format(count))
count = len(shipped_orders)
if count > 5:
	print("\nYou have {} confirmed orders that have shipped, coooook!".format(count))
else:
	print("\nYou have {} confirmed orders that have shipped!".format(count))
input("\npress enter to close...")