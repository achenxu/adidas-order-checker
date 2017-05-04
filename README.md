# adidas-order-checker
Checks the status of adidas online orders

At the moment this only works for adidas UK, US, FR and DE. If someone can provide me with an order # and email for their locale then I can add support for it :)

Instructions:
- Git clone into the repository or download the zip file
- You need python 3+ to run and you need requests and bs4 installed (this can be done with `pip install requests` and `pip install bs4` respectively
- You must then put the details of the orders you want to check in the orders.txt file in the format `ordernumber:email` DO NOT FORGET THE : (no spaces)
- Then run order-checker.py

Please let me know what bugs you find cos I haven't tested it much...
