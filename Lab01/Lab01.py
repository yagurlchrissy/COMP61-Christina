# Part 1: Setup Variables / Part 2: User Input

temperature = int(input("Enter the current temperature (in degrees): ")) budget = float(input("Enter your available budget: "))

weather_condition = input("Enter the current weather condition (sunny, rainy, cloudy): ")

# Part 3: Decision Logic / Part 4: Output

if weather_condition == "sunny":

    if temperature > 75:

       if budget > 20.00:

          print("Go to the beach!")

       else:

            print("Have a picnic in the park.")

elif weather_condition == "rainy":

       if budget > 15.00:

          print("Visit a museum.")

       else:

           print("Stay in and watch a movie at home.")

elif weather_condition == "cloudy" or temperature < 60:

       print("Go to a coffee shop and enjoy a warm drink." )

else: 

print("Make your own adventure!")