DIET AND RATION COMPANION

<strong>The project aims to</strong>:
- Calculating user's basal metabolic rate.
- Fetching a specific macronutrient of any available product.
- Suggesting a diet/diet variety for a user by sorting the products based on their nutritional value (macronutrients: protein, fat, carbs, fiber, calories) specified by user.

<strong>Available commands are</strong>:
- Calculate basal metabolic rate (bmr) for male/female (_calculate_bmr() function) - <b>"calculate bmr"</b> input -> multiple prompts for calculating ->  result is formatted as a rounded float of calories used by user's body during a regular day (activity factor applies as a multiplier to a result of equation).
- Show a list of products (show_products() function) - <b>"show products"</b> input -> products_list prints out.
- Show macros for a specific product (show_macros() function) - <b>"show macros"</b> input -> input of a product name from the products dict.
- Show a user specified macronutrient of a product (_get_nested_val() + main() functions) - <b>"show specifics"</b> input -> input of a product name and then - the macronutrient in question.
- Printing out a list of available products sorted by macronutrient (specified by user) content in descending order (main() function) - <b>"suggest"</b> input. -> input of a macronutrient ("protein", "fat", "carbs", "fiber", "calories").

All of the nutritional values were taken from https://www.verywellfit.com/

The formulas and activity factors were taken from https://www.omnicalculator.com/health/bmr-harris-benedict-equation#what-is-the-harris-benedict-equation


Creating a <b>custom class Nutrients</b> allows for easier manipulation with dict's values

<b>main()</b> function is for telling the programm what to execute, except when _get_nested_value() or Nutrients custom class are called:
- in case of an input of "show specific" - main() prompts the user for two inputs right away, then calls the _get_nested_val() function and prints a string with user specified product and macronutrient;
output differs depending on a macronutrient specified - "grams of" fragment is for protein, fat, carbs and fiber. "calories in" fragment is for calories.
- in case of an input of "suggest" - main()

<b>_get_nested_val()</b> function gets and then returns the value of any key in products dict.
This function makes it possible for the user to choose any product from the available list and specify a macronutrient of interest.

<b>show_products()</b> function is a simple output of all products unpacked as a list. Useful for familiarizing the user with available products.

<b>show_macros()</b> function outputs nutritional information of an inputted product. Can be used in case user wants to see all macronutrients for a specified product.

<b>_calculate_brm()</b> function will ask the user for a few inputs to process them into Harris-Benedict equation (two different equations for male and female users).
Outputs the user's basal metabolic rate, depending on daily physical activity chosen from the list (activity_options dict);
physical activity factor multiplies the base basal metabolic rate by a activity_options dict's value (act_mult variable).
