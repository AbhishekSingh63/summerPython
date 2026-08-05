import matplotlib.pyplot as plt
from data_loader import *

# blood group distribution bar chart
def blood_group_chart():

    blood_groups = donors["blood_group"].value_counts()

    plt.figure(figsize=(8,5))

    plt.bar(
        blood_groups.index,
        blood_groups.values
    )

    plt.title("Blood Group Distribution")

    plt.xlabel("Blood Group")

    plt.ylabel("Number of Donors")

    plt.show()

# blood stock pie chart
def blood_stock_chart():

    plt.figure(figsize=(7,7))

    plt.pie(
        blood_stock["units_available"],
        labels=blood_stock["blood_group"],
        autopct="%1.1f%%"
    )

    plt.title("Blood Stock Distribution")

    plt.show()

# city wise donors
def city_donor_chart():

    city = donors["city"].value_counts()

    plt.figure(figsize=(8,5))

    plt.bar(
        city.index,
        city.values
    )

    plt.title("City-wise Donors")

    plt.xlabel("City")

    plt.ylabel("Donors")

    plt.xticks(rotation=30)

    plt.show()

# donor age distribution histogram
def age_distribution():

    plt.figure(figsize=(8,5))

    plt.hist(
        donors["age"],
        bins=6
    )

    plt.title("Donor Age Distribution")

    plt.xlabel("Age")

    plt.ylabel("Frequency")

    plt.show()




from utils import heading, pause

def chart_menu():

    while True:

        heading("Charts")

        print("1. Blood Group Distribution")

        print("2. Blood Stock Distribution")

        print("3. City-wise Donors")

        print("4. Donor Age Distribution")

        print("0. Back")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            blood_group_chart()

        elif choice == "2":
            blood_stock_chart()

        elif choice == "3":
            city_donor_chart()

        elif choice == "4":
            age_distribution()

        elif choice == "0":
            break

        else:
            print("Invalid Choice")

        pause()