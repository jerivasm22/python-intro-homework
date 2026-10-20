day_week = input("What day is it?: ").lower()
time_day = input("What time of day?: ").lower()
if day_week == "monday" and time_day == "morning":
    print("Suggestion: I am very sorry, but you will be working at that time.")
elif day_week == "monday" and time_day == "afternoon":
    print("Suggestion: A good day to play pickleball with your friends")
elif day_week == "monday" and time_day == "evening":
    print("Suggestion: Full Python study night")
elif day_week == "friday" and time_day == "morning":
    print("Suggestion: We should start the day with some exercise, so we will go hiking.")
elif day_week == "friday" and time_day == "afternoon":
    print("Suggestion: Getting together for lunch with my friends to share experiences")
elif day_week == "friday" and time_day == "evening":
    print("Suggestion: Dinner with my wife at a nice restaurant")
elif day_week == "sunday" and time_day == "morning":
    print("Suggestion: Go to the market to restock the pantry for the week")
elif day_week == "sunday" and time_day == "afternoon":
    print("Suggestion: Doing laundry and cleaning the house while listening to music")
elif day_week == "sunday" and time_day == "evening":
    print("Suggestion: Watch a movie and eat snacks")
else:
    print("Sorry, I don't recognize that day. Try: Monday, Friday and Sunday.")