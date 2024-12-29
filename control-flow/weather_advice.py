cureent_weather = "sunny"
print(f"What's the weather like today? (sunny/rainy/cold): {cureent_weather}")
if cureent_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif cureent_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif cureent_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")