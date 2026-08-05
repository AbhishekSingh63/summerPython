import numpy as np
from data_loader import *
from utils import heading




# Data Cleaning and Preparation
def data_overview():
    heading("DONORS DATASET OVERVIEW")

    print("\nFirst 5 Records")
    print(donors.head())

    print("\nShape")
    print(donors.shape)

    print("\nColumns")
    print(donors.columns.tolist())

    print("\nInformation")
    donors.info()

    print("\nSummary Statistics")
    print(donors.describe())

def check_missing_values():
    print("\nMissing Values")
    print("*" * 50)
    print(donors.isnull().sum())


def check_duplicates():
    print("\nDuplicate Records")
    print("*" * 50)

    duplicates = donors.duplicated().sum()
    print("Duplicate Rows :", duplicates)

def remove_duplicates():
    global donors

    before = len(donors)

    donors = donors.drop_duplicates()

    after = len(donors)

    print("\nDuplicate Removal")
    print("*" * 50)
    print("Rows Before :", before)
    print("Rows After  :", after)

def rename_columns():
    global donors

    donors.rename(
        columns={
            "donor_name": "Name",
            "blood_group": "Blood Group"
        },
        inplace=True
    )

    print("\nUpdated Columns")
    print(donors.columns.tolist())

def convert_age():
    global donors

    donors["age"] = donors["age"].astype(float)

    print(donors.dtypes)

def blood_group_count():
    print("\nBlood Group Count")

    print(
        donors["Blood Group"].value_counts()
    )




# Data Analysis

def total_donors():
    heading("TOTAL DONORS")

    total = len(donors)

    print("Total Donors :", total)

def average_age():
    heading("AVERAGE DONOR AGE")

    avg = np.mean(donors["age"])

    print(f"Average Age : {avg:.2f} years")

def blood_group_distribution():

    heading("BLOOD GROUP DISTRIBUTION")

    print(donors["blood_group"].value_counts())

def city_wise_donors():

    heading("CITY-WISE DONORS")

    city = donors.groupby("city")["donor_id"].count()

    print(city)

def blood_stock_summary():

    heading("BLOOD STOCK")

    print(blood_stock)

def hospital_patients():

    heading("HOSPITAL-WISE PATIENTS")

    merged = patients.merge(
        hospitals,
        on="hospital_id"
    )

    report = merged.groupby(
        "hospital_name"
    )["patient_id"].count()

    print(report)