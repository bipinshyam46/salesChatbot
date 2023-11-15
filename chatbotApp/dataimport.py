import  sqlite3
import json

# connection
#  the loaded data are added to intents.json file
existing_data = json.loads(open('intents.json').read())
db_sqlite = r'C:\Users\bipin\OneDrive\Desktop\Chatbot\chatbotProject\db.sqlite3'

con = sqlite3.connect(db_sqlite)
cursor = con.cursor()

#  query to check total available products
sql_query1 = "SELECT name FROM chatbotApp_product WHERE  availability_status ==1"
cursor.execute(sql_query1)
total_available_products = cursor.fetchall()


new_intent = {
"tag": "questions",
"patterns": ["what products do you sell","what are the products available","list available products"],
"responses": [f"we have {total_available_products} available"],
"context": [""]
}

# existing_data.append(new_intent)
existing_data['intents'].append(new_intent)
with open('intents.json', 'w') as file:
    json.dump(existing_data, file, indent=2)



# #  query to check availability of products
sql_query2 = "SELECT name,tag FROM chatbotApp_product WHERE  availability_status ==1"
cursor.execute(sql_query2)
available_products = cursor.fetchall()
dict_available_products = dict(available_products)

for key,value in dict_available_products.items():
    new_intent = {
    "tag": f"{value}",
    "patterns": [f"is {key} available"],
    "responses": [f" {key} is available"],
    "context": [""]
    }
    # Add the new intent to the existing data
    existing_data["intents"].append(new_intent)
    # existing_data.update(new_intent)
    with open('intents.json', 'w') as file:
        json.dump(existing_data, file, indent=2)

#  query to check price of products
sql_query1 = "SELECT name,price FROM chatbotApp_product"
cursor.execute(sql_query1)
product_price = cursor.fetchall()
dict_product_price = dict(product_price)

for key,value in dict_product_price.items():
    new_intent = {
    "tag": f"{key}",
    "patterns": [f" price {key}"],
    "responses": [f"{value} rupees"],
    "context": [""]
    }
    # Add the new intent to the existing data
    existing_data["intents"].append(new_intent)
    # existing_data.update(new_intent)
    with open('intents.json', 'w') as file:
        json.dump(existing_data, file, indent=2)

