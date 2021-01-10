import numpy as np
import pandas as pd

ecom_import = pd.read_csv("..\Ecommerce Purchases")

ecom = pd.DataFrame(ecom_import)

ecom_head = ecom.head(2)
print(ecom_head)

print("Rows and Columns")
print(ecom.info())

print("Average purchase price")
print(ecom["Purchase Price"].mean())

print("Max purchase price")
print(ecom["Purchase Price"].max())

print("Min purchase price")
print(ecom["Purchase Price"].min())

print("English as language of choice")
print(ecom[ecom["Language"] == "en"].count()) 

print("Lawyer Job title")
print(ecom[ecom["Job"] == "Lawyer"].count())

print("AM Purchase")
print(sum(ecom[ecom["AM or PM"] == "AM"].value_counts()))

print("PM Purchase")
print(sum(ecom[ecom["AM or PM"] == "PM"].value_counts()))

print("AM VS PM One Line")
print(ecom["AM or PM"].value_counts())

print(" Five most common job titles")
print(ecom["Job"].value_counts(5).head())

print("Find the value of a purchase")
print(ecom[ecom["Lot"] == "90 WT"]["Purchase Price"])

print("Find the email from the card number")
print(ecom[ecom["Credit Card"] == 4926535242672853]["Email"])

print("American express and have spent over $95")
print(ecom[(ecom["CC Provider"] == "American Express") & (ecom["Purchase Price"] > 95)].count())

print("Credit card that expires in 2025")
print(sum(ecom["CC Exp Date"].apply(lambda exp: exp[3:]=="25")))
# The credit card exp date is a string. Check it first. Then you can select the year with the Lambdas and [:]

print("Most popular email address domains")
print(ecom["Email"].apply(lambda x : x.split("@")[1]).value_counts().head(5))