## Adidas Order Checker
Checks the status of adidas online orders. At the moment this supports adidas UK, US, FR and DE. I can add support for other locales if I am provided with an order for that locale as an example. With the release of V2, it is now easier for users themselves to add their own locale if they have basic common sense. Simply add a new locale to the `locales.json` file, following the same template that is shown in the file.

## Instructions
- Git clone into the repository or download the zip file
- You need python 3+ to run and you need requests and bs4 installed (this can be done with `pip install requests` and `pip install bs4` respectively)
- You must then put the details of the orders you want to check in the orders.txt file in the format `ordernumber:email` DO NOT FORGET THE : (no spaces)
- Then run `main.py`

## FAQ
**Will you help me?** No. I am very busy and this is not something that I will provide support for. However, if you find a BUG then pls contact me or open an issue.
