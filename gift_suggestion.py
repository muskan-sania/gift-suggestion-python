import random

gifts = {
    "low": {
        "birthday": ["Bouquet", "Chocolate", "Photo frame"],
        "anniversary": ["Card", "Flowers", "Chocolate box"],
        "eid": ["Sweets", "Dates", "Chocolates"],
        "festival": ["Sweets", "Candles", "Decor items"]
    },
    "high": {
        "birthday": ["Watch", "Shoes", "Customized gift"],
        "anniversary": ["Dinner set", "Couple watch", "Photo album"],
        "eid": ["Clothes", "Perfume", "Gift hamper"],
        "festival": ["Clothes", "Decor set", "Gift box"]
    }
}


def get_occasion(choice):
    options = {
        1: "birthday",
        2: "anniversary",
        3: "eid",
        4: "festival"
    }
    return options.get(choice, None)


def suggest_gift(budget, occasion, person):
    category = "low" if budget <= 500 else "high"

    if occasion in gifts[category]:
        suggestions = random.sample(gifts[category][occasion], 2)
        print(f"\nGift ideas for {person}:")
        for gift in suggestions:
            print(f"- {gift}")
    else:
        print("Invalid occasion!")


while True:
    print("\n======  Gift Suggestion App ======")

    try:
        budget = int(input("Enter your budget: "))
    except:
        print("Please enter a valid number!")
        continue

    print("\nChoose Occasion:")
    print("1. Birthday")
    print("2. Anniversary")
    print("3. Eid")
    print("4. Festival")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except:
        print("Invalid input!")
        continue

    occasion = get_occasion(choice)
    if not occasion:
        print("Invalid choice!")
        continue

    person = input("Enter the person name: ")

    suggest_gift(budget, occasion, person)

    again = input("\nDo you want another suggestion? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the app ")
        break