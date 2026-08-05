import pandas as pd

# Load all CSV files
donors = pd.read_csv("data/donors.csv")
donations = pd.read_csv("data/donations.csv")
patients = pd.read_csv("data/patients.csv")
hospitals = pd.read_csv("data/hospitals.csv")
blood_stock = pd.read_csv("data/blood_stock.csv")
blood_requests = pd.read_csv("data/blood_requests.csv")