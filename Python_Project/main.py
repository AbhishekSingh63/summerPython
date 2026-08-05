from utils import heading, pause

# Import analysis functions
from analysis import *

# Import chart functions
from charts import *

# Import datasets
from data_loader import *

while True:

    heading("Blood Bank Analytics Dashboard")

    print("Python Summer Training Project")
    print("\nTechnology Used")
    print("- Python")
    print("- NumPy")
    print("- Pandas")
    print("- Matplotlib")

    print("\n============== MAIN MENU ==============")
    print("1. Inspect Dataset")
    print("2. Data Cleaning")
    print("3. Data Analysis")
    print("4. Data Visualization")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    # ==========================
    # INSPECT DATASET
    # ==========================

    if choice == "1":

        heading("Inspect Dataset")

        print("\nFirst 5 Records")
        print(donors.head())

        print("\nLast 5 Records")
        print(donors.tail())

        print("\nShape")
        print(donors.shape)

        print("\nColumns")
        print(donors.columns)

        print("\nDataset Information")
        donors.info()

        print("\nStatistical Summary")
        print(donors.describe())

        pause()

    # ==========================
    # DATA CLEANING MENU
    # ==========================

    elif choice == "2":

        while True:

            heading("Data Cleaning")

            print("1. Dataset Overview")
            print("2. Missing Values")
            print("3. Duplicate Records")
            print("4. Remove Duplicates")
            print("5. Rename Columns")
            print("6. Convert Data Type")
            print("7. Blood Group Count")
            print("0. Back")

            clean = input("\nEnter your choice: ")

            if clean == "1":
                data_overview()

            elif clean == "2":
                check_missing_values()

            elif clean == "3":
                check_duplicates()

            elif clean == "4":
                remove_duplicates()

            elif clean == "5":
                rename_columns()

            elif clean == "6":
                convert_age()

            elif clean == "7":
                blood_group_count()

            elif clean == "0":
                break

            else:
                print("Invalid Choice")

            pause()

    # ==========================
    # DATA ANALYSIS MENU
    # ==========================

    elif choice == "3":

        while True:

            heading("Data Analysis")

            print("1. Total Donors")
            print("2. Average Donor Age")
            print("3. Blood Group Distribution")
            print("4. City-wise Donors")
            print("5. Blood Stock Summary")
            print("6. Hospital-wise Patients")
            print("0. Back")

            analysis_choice = input("\nEnter your choice: ")

            if analysis_choice == "1":
                total_donors()

            elif analysis_choice == "2":
                average_age()

            elif analysis_choice == "3":
                blood_group_distribution()

            elif analysis_choice == "4":
                city_wise_donors()

            elif analysis_choice == "5":
                blood_stock_summary()

            elif analysis_choice == "6":
                hospital_patients()

            elif analysis_choice == "0":
                break

            else:
                print("Invalid Choice")

            pause()

    # ==========================
    # CHART MENU
    # ==========================

    elif choice == "4":

        while True:

            heading("Data Visualization")

            print("1. Blood Group Distribution")
            print("2. Blood Stock Distribution")
            print("3. City-wise Donors")
            print("4. Donor Age Distribution")
            print("0. Back")

            chart = input("\nEnter your choice: ")

            if chart == "1":
                blood_group_chart()

            elif chart == "2":
                blood_stock_chart()

            elif chart == "3":
                city_donor_chart()

            elif chart == "4":
                age_distribution()

            elif chart == "0":
                break

            else:
                print("Invalid Choice")

    # ==========================
    # EXIT
    # ==========================

    elif choice == "0":

        heading("Thank You")

        print("Thank you for using")
        print("Blood Bank Analytics Dashboard")

        break

    else:

        print("\nInvalid Choice")
        pause()