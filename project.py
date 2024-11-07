from collections import UserDict

products = {
    "almonds": {"protein": 6.0, "fat": 14.2, "carbs": 6.1, "fiber": 3.5, "calories": 164},
    "apple": {"protein": 0.5, "fat": 0.3, "carbs": 27.6, "fiber": 4.8, "calories": 104},
    "avocado": {"protein": 2.0, "fat": 14.7, "carbs": 8.5, "fiber": 6.7, "calories": 160},
    "banana": {"protein": 1.3, "fat": 0.4, "carbs": 27.0, "fiber": 3.1, "calories": 105},
    "beef": {"protein": 26.0, "fat": 7.6, "carbs": 0, "fiber": 0, "calories": 179},
    "beer": {"protein": 0.7, "fat": 0, "carbs": 3.0, "fiber": 0, "calories": 99.4},
    "blue cheese": {"protein": 6.1, "fat": 8.1, "carbs": 0.7, "fiber": 0, "calories": 100},
    "buckwheat": {"protein": 5.7, "fat": 1.0, "carbs": 34.0, "fiber": 4.5, "calories": 155},
    "brown rice": {"protein": 4.5, "fat": 1.6, "carbs": 45.6, "fiber": 3.5, "calories": 218},
    "cheddar cheese": {"protein": 7.0, "fat": 10.0, "carbs": 0, "fiber": 0, "calories": 120},
    "chicken breast": {"protein": 26.0, "fat": 2.7, "carbs": 0, "fiber": 0, "calories": 128},
    "chicken egg": {"protein": 6.0, "fat": 5.0, "carbs": 0.6, "fiber": 0.6, "calories": 78},
    "cottage cheese": {"protein": 11.0, "fat": 2.3, "carbs": 4.3, "fiber": 0, "calories": 84},
    "corn": {"protein": 3.3, "fat": 1.4, "carbs": 19.0, "fiber": 2.0, "calories": 88},
    "ground beef": {"protein": 24.0, "fat": 13, "carbs": 0, "fiber": 0, "calories": 218},
    "milk": {"protein": 8.0, "fat": 4.6, "carbs": 12.0, "fiber": 0, "calories": 122},
    "hazelnuts": {"protein": 4.2, "fat": 17.0, "carbs": 4.7, "fiber": 2.8, "calories": 178},
    "oatmeal": {"protein": 5.0, "fat": 2.5, "carbs": 28.0, "fiber": 4.0, "calories": 140},
    "peanuts": {"protein": 7.3, "fat": 14.0, "carbs": 4.6, "fiber": 2.4, "calories": 161},
    "peanut butter": {"protein": 7.0, "fat": 16.0, "carbs": 8.0, "fiber": 2.0, "calories": 190},
    "potato": {"protein": 4.6, "fat": 0.2, "carbs": 37.0, "fiber": 4.0, "calories": 164},
    "pork": {"protein": 22.0, "fat": 3.0, "carbs": 0, "fiber": 0, "calories": 122},
    "salmon": {"protein": 17.0, "fat": 5.4, "carbs": 0, "fiber": 0, "calories": 121},
    "sweet potato": {"protein": 3.6, "fat": 0.1, "carbs": 37, "fiber": 3.9, "calories": 162},
    "yogurt": {"protein": 8.5, "fat": 8.0, "carbs": 11.4, "fiber": 0, "calories": 149},
    "white rice": {"protein": 4.4, "fat": 0.4, "carbs": 53.4, "fiber": 0.6, "calories": 242},
    "quinoa": {"protein": 8.0, "fat": 4.0, "carbs": 39.0, "fiber": 5.0, "calories": 222},
}

products_list = [
            "Almonds", "Apple", "Avocado", "Banana", "Beef", "Beer",
            "Blue cheese", "Brown rice", "Buckwheat", "Cheddar cheese",
            "Chicken breast", "Chicken egg", "Corn", "Cottage cheese",
            "Ground beef", "Hazelnuts", "Milk", "Oatmeal", "Peanut butter",
            "Peanuts", "Pork", "Potato", "Quinoa", "Salmon",
            "Sweet potato", "White rice", "Yogurt"
]


class Nutrients(UserDict):
    MN = ["protein", "fat", "carbs", "fibre", "calories"]

    def __init__(self, *args):
        super().__init__()
        assert len(args) == len(Nutrients.MN)
        self.data = dict(zip(Nutrients.MN, args))

products: dict[str, Nutrients] = {
    "almonds": Nutrients(6.0, 14.2, 6.1, 3.5, 164),
    "apple": Nutrients(0.5, 0.3, 27.6, 4.8, 104),
    "avocado": Nutrients(2.0, 14.7, 8.5, 6.7, 160),
    "banana": Nutrients(1.3, 0.4, 27.0, 3.1, 105),
    "beef": Nutrients(26.0, 7.6, 0, 0, 179),
    "beer": Nutrients(0.7, 0, 3.0, 0, 99.4),
    "blue cheese": Nutrients(6.1, 8.1, 0.7, 0, 100),
    "buckwheat": Nutrients(5.7, 1.0, 34.0, 4.5, 155),
    "brown rice": Nutrients(4.5, 1.6, 45.6, 3.5, 218),
    "cheddar cheese": Nutrients(7.0, 10.0, 0, 0, 120),
    "chicken breast": Nutrients(26.0, 2.7, 0, 0, 128),
    "chicken egg": Nutrients(6.0, 5.0, 0.6, 0.6, 78),
    "cottage cheese": Nutrients(11.0, 2.3, 4.3, 0, 84),
    "corn": Nutrients(3.3, 1.4, 19.0, 2.0, 88),
    "ground beef": Nutrients(24.0, 13, 0, 0, 218),
    "milk": Nutrients(8.0, 4.6, 12.0, 0, 122),
    "hazelnuts": Nutrients(4.2, 17.0, 4.7, 2.8, 178),
    "oatmeal": Nutrients(5.0, 2.5, 28.0, 4.0, 140),
    "peanuts": Nutrients(7.3, 14.0, 4.6, 2.4, 161),
    "peanut butter": Nutrients(7.0, 16.0, 8.0, 2.0, 190),
    "potato": Nutrients(4.6, 0.2, 37.0, 4.0, 164),
    "pork": Nutrients(22.0, 3.0, 0, 0, 122),
    "salmon": Nutrients(17.0, 5.4, 0, 0, 121),
    "sweet potato": Nutrients(3.6, 0.1, 37, 3.9, 162),
    "yogurt": Nutrients(8.5, 8.0, 11.4, 0, 149),
    "white rice": Nutrients(4.4, 0.4, 53.4, 0.6, 242),
    "quinoa": Nutrients(8.0, 4.0, 39.0, 5.0, 222)
}


def main():
    initial = input("What do you want the programm to do? ").lower().strip()
    if initial == "show products":
        show_products()
    elif initial == "show macros":
        show_macros(initial)
    elif initial == "calculate bmr":
        _calculate_bmr()
    elif initial == "show specifics":
            product = input("Enter the name of a product: ").lower().strip()
            call = input("Enter a macro: ").lower().strip()
            if call == "protein" or call == "fat" or call == "carbs" or call == "fiber":
                print(_get_nested_val(products, product, call), "grams of", call, "in", product.capitalize())
            elif call == "calories":
                print(_get_nested_val(products, product, call), "calories in", product.capitalize())
    elif initial == "suggest":
        mn = input("Enter a macronutrient: ")
        if mn in Nutrients.MN:
            print(f"List of products by {mn} content in descending order:")
        for p, *_ in sorted(products.items(), key=lambda t: t[1][mn], reverse=True):
            print(f"\b{p.capitalize()[mn]}")


def _get_nested_val(data, *args):
    if args and data:
        element  = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else _get_nested_val(value, *args[1:])


def show_products():
    print("Products:", *products, sep = "\n -")


def show_macros(product):
    product = input("Enter the name of a product: ").lower().strip()
    if product in products:
        result = (f"Nutritional value of the product: {products[product]}")
        print(result)
    else:
        raise ValueError("Please, enter the correct name of a product")


def _calculate_bmr():
    gender = input("Enter your gender male/female: ").lower().strip()
    age = int(input("Enter your age: "))
    height = int(input("Enter your height in cm: "))
    weight = int(input("Enter your weight in kg: "))

    activity_options = {
        "1 - little or no exercise": 1.2,
        "2 - light exercise/sports 1-3 days/week": 1.375,
        "3 - moderate exercise/sports 3-5 days/week": 1.55,
        "4 - hard exercise/sports 6-7 days a week": 1.725,
        "5 - very hard exercise/sports & a physical job": 1.9,
        "6 - If you train as a professional athlete": 2.3
    }

    print("What is your activity factor?", *activity_options, sep = "\n")
    activity = int(input("Choose the number corresponding to your daily activity: "))

    if activity == 1:
        act_mult = activity_options.get("1 - little or no exercise")
    elif activity == 2:
        act_mult = activity_options.get("2 - light exercise/sports 1-3 days/week")
    elif activity == 3:
        act_mult = activity_options.get("3 - moderate exercise/sports 3-5 days/week")
    elif activity == 4:
        act_mult = activity_options.get("4 - hard exercise/sports 6-7 days a week")
    elif activity == 5:
        act_mult = activity_options.get("5 - very hard exercise/sports & a physical job")
    elif activity == 6:
        act_mult = activity_options.get("6 - If you train as a professional athlete")
    else:
        raise ValueError("Invalid activity option")

    if gender == "male":
        bmr_male = (66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)) * act_mult
        print(round(bmr_male), "kcal")
    elif gender == "female":
        bmr_female = (655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)) * act_mult
        print(round(bmr_female), "kcal")
    else:
        raise ValueError("This programm is not that sophisticated")


if __name__ == "__main__":
    main()
