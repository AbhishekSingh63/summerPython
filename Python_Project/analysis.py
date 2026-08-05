import numpy as np
from data_loader import *

def data_overview():
    print("=" * 60)
    print("DONORS DATASET OVERVIEW")
    print("=" * 60)

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
    print("-" * 40)
    print(donors.isnull().sum())


def check_duplicates():
    print("\nDuplicate Records")
    print("-" * 40)

    duplicates = donors.duplicated().sum()
    print("Duplicate Rows :", duplicates)

def remove_duplicates():
    global donors

    before = len(donors)

    donors = donors.drop_duplicates()

    after = len(donors)

    print("\nDuplicate Removal")
    print("-" * 40)
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



def total_donors():
    print("\n" + "="*50)
    print("TOTAL DONORS")
    print("="*50)

    total = len(donors)

    print("Total Donors :", total)

def average_age():
    print("\n" + "="*50)
    print("AVERAGE DONOR AGE")
    print("="*50)

    avg = np.mean(donors["age"])

    print(f"Average Age : {avg:.2f} years")

def blood_group_distribution():

    print("\n" + "="*50)
    print("BLOOD GROUP DISTRIBUTION")
    print("="*50)

    print(donors["blood_group"].value_counts())

def city_wise_donors():

    print("\n" + "="*50)
    print("CITY-WISE DONORS")
    print("="*50)

    city = donors.groupby("city")["donor_id"].count()

    print(city)

def blood_stock_summary():

    print("\n" + "="*50)
    print("BLOOD STOCK")
    print("="*50)

    print(blood_stock)

def hospital_patients():

    print("\n" + "="*50)
    print("HOSPITAL-WISE PATIENTS")
    print("="*50)

    merged = patients.merge(
        hospitals,
        on="hospital_id"
    )

    report = merged.groupby(
        "hospital_name"
    )["patient_id"].count()

    print(report)