#this is how to make a pipeline data 

#1. import all the library
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
<<<<<<< HEAD
from dotenv import load_dotenv
=======
>>>>>>> 9a755d1 (Add Docker Compose and environment template)
import os
#2. connect to the API
url= "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data =response.json()

#3.convert json into a DataFrame
df= pd.DataFrame(data) # now I have a table that in dataFrame

#4. cleaning the data, like for example i only need the name,email and company name columns
df["company_name"] = df["company"].apply(  #this function because the company namw is inside the address
    lambda company : company["name"]
)
df = df[[
    "name",
    "email",
    "company_name"
]]

# Keep only companies containing "Group"
df = df[df["company_name"].str.contains("Group")] #does the string contain group  

#5. connect to PostgreSQL
load_dotenv()

engine = create_engine(
    f"postgresql+psycopg://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


#6. save the data to the database (Postgresql)
df.to_sql(
    "customers", #instead of employees (this is the name of the table in the data base)
    engine,
    if_exists="replace",
    index=False
)

#7. reading the data from PostgreSQL
query = "SELECT * FROM customers"
customers_df= pd.read_sql(query, engine) #reading from database and save it in python as DataFrame

# 8. save it as Parquet
customers_df.to_parquet(
    "customers.parquet",
    index=False
)

#9. print
print(customers_df)

