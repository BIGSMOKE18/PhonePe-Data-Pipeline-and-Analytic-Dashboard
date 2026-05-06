import json
import pandas as pd
import os

base_path = "state"
rows=[] #Empty list to store dataq

for state in os.listdir(base_path):
    states_path = os.path.join(base_path,state)

    if os.path.isdir(states_path):
        
        for year in os.listdir(states_path):
            year_path = os.path.join(states_path,year)

            if os.path.isdir(year_path):

                for file_name in os.listdir(year_path):
                    if file_name.endswith(".json"):
                       quarter = "Q" + file_name.split(".")[0]
                       file_path = os.path.join(year_path,file_name)

                       with open(file_path, 'r') as file:
                            data = json.load(file)

                       transactions = data["data"]["transactionData"]

                       for item in transactions:
                        category = item["name"]
                        count = item["paymentInstruments"][0]["count"]
                        amount = item["paymentInstruments"][0]["amount"]

                        rows.append([
                            state.title(),
                            year,
                            quarter,
                            category,
                            count,
                            amount
                        ])
                    


df = pd.DataFrame(rows, columns = ["State", "Year", "Quarter", "Category", "Count","Amount"])
#df.to_csv("full_data.csv", index = False)
#print(df.head())

#print(df.isnull().sum())

df = df.dropna()
df = df.drop_duplicates()

df["Year"] = df["Year"].astype(int)
df["Count"] = df["Count"].astype(int)
df["Amount"] = df["Amount"].astype(float)

df["State"] = df["State"].str.title()

df = df.reset_index(drop = True)

df.to_csv("cleaned_data.csv", index = False)


# database creation 

import sqlite3

conn = sqlite3.connect("phone_pe.db")

df.to_sql("transactions", conn, if_exists="replace", index=False)

#TOP 5 STATES WITH HIGHEST TRANSACTIONS(AMOUNT) VIA PHONE PE 
query = """SELECT State, SUM(Amount) as Total_Amount
FROM transactions
GROUP BY State
ORDER BY Total_Amount DESC
LIMIT 5;
 """

cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
print("TOP 5 Performing States")
for row in rows:
    print(row)

#TOP CATEGORY
query2 = """
SELECT Category, SUM(Amount) as Total_Amount
FROM transactions
GROUP BY Category
ORDER BY Total_Amount DESC
 """

cursor.execute(query2)
rows2 = cursor.fetchall()
print("TOP Category")
for row in rows2:
    print(row)

 # YEAR WISE GROWTH
query3 = """
 SELECT Year, SUM(Amount) as Total_Amount
 FROM transactions
 GROUP BY Year
 ORDER BY Year
 """   
cursor.execute(query3)
print("Year-Wise Growth")
rows3 = cursor.fetchall()
for row in rows3:
    print(row)

conn.close()