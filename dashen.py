from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://dashenbanksc.com/daily-exchange-rate"
path = r'C:\Users\Mihretu\Downloads\chromedriver-win64/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# driver.find_elements(By.TAG_NAME, 'tr')
column_name = []
currency_code =[]
currency_name = []
cash_buying = []
cash_selling =[]


currency_table = driver.find_elements(By.TAG_NAME, 'tr')

for data in currency_table:
    cells = data.find_elements(By.TAG_NAME, 'td')
    # print(len(cells))
    if cells:
        # appending 'none' to empty values
        currency_code.append(cells[0].text if cells[0].text.strip() else None)
        currency_name.append(cells[1].text if cells[1].text.strip() else None)
        cash_buying.append(cells[2].text if cells[2].text.strip() else None)
        cash_selling.append(cells[3].text if cells[3].text.strip() else None)
# filer the none parts
currency_code = [item for item in currency_code if item]
currency_name = [item for item in currency_name if item]
cash_buying = [item for item in cash_buying if item]
cash_selling = [item for item in cash_selling if item]
# print(currency_code)
# print(currency_name)
# print(cash_buying)
# print(cash_selling)



whole_data = [ 
    currency_code,
    currency_name,
    cash_buying,
    cash_selling
]
for sublist in whole_data:
    column_name.append(sublist[0])
print(column_name)
    
columns = column_name
    
data = [ 
    currency_code[1:],
    currency_name[1:],
    cash_buying[1:],
    cash_selling[1:]
]
#Transposing the data since they are row in column and vise versa
transposed_data = list(map(list, zip(*data)))
print (transposed_data)

df = pd.DataFrame(transposed_data, columns=column_name )
# # Example debugging step
# for i, row in enumerate(data):
#     print(f"Row {i}: {row} (Length

df.to_csv('dashen_scraped_data.csv', index=False)
driver.quit()