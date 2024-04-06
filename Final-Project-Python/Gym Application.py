#Gym Application

import time
import datetime

actual_date = datetime.datetime.now()
one_month_later = actual_date + datetime.timedelta(days=30)


#User registration

print('\nWelcome to the gym Olimpia, since it is your first time here, lets create your username!')

while True:
    
        new_username = input('\nPlease create your username: ')
        new_password = input('Please create a password: ')
        print(f'You have succefully enrolled, welcome! {new_username}\n')
        break



#Class and Schedule Booking
#Class schedules and availability
def class_schedule():
    class_schedule = input('\nThe classes available are the following: \n1->Cardio Classes, Available each week only on Monday and Friday at 7am. \n2->Yoga classes, available each week only on Wendsday at 8am\nWould you like to book any of those two? \n1 for Exit\n2 for Cardio\n3 for Yoga\n')
    if class_schedule != '1' and class_schedule != '2' and class_schedule != '3':
        print('You seleccted the wrong option, please try again')
    elif class_schedule == '2':
        print(f'{new_username}, you have succefully been enrolled in Cardio classes, see you soon!')
        time.sleep(5)
    elif class_schedule == '3': 
        print(f'{new_username}, you have succefully been enrolled in Yoga classes, see you soon!')
        time.sleep(5)
    elif class_schedule == '1':
        print('See you soon!')
    return class_schedule

# Workout Tracking

# Progress tracking (weights)


def workout_training(weight, weights):
    
    
    
    weight.append(weights)
    print('Your current weight is: ', weight, 'See you next month with the next weight and hope to see some progress!')
    time.sleep(5)
    return workout_training


#Gym menu
while True:
    menu = input("\nHere you have all the options for the Olimpia Gym: \n1->Membership Management \n2->Class and Schedule Booking \n3->Nutrition and Diet \n4->Workout Tracking \n5->Trainer's name \n6->Gym exercises \n7->Exit: \n")
    if menu == '0' and menu > '7':
        print('You selected the wrong option, please try again')

#Membership Management information
#Membership plans
    elif menu == '1':
        membership = input('\n1->Membership plans and pricing \n2->Online payment processing \n3->Exit.\n')
        if membership == '0' and membership > '4':
            print('You selected the wrong option, please try again')
        elif membership == '1':
            print('\nThe plans and pricing are the following: \n$25 each month, only the gym is included. \n1->$35 each month, gym and yoga is included. \n2->$45 each month, gym, yoga and spinning is included. \n3->$65 each month, gym, yoga, spinning and nutricionist is included')
            time.sleep(10)
        elif membership == '2':
            payment = input('\nIf you already know the plans(from Membership plans and pricing option), please select the plan that you want: ')
            if payment == '0' and payment >3:
                print('You selected the wrong option, please try again: ')
            elif payment == '1':
                payment_1 = input(f'\nYou have selected the plan #1: Only the gym is included, for the amount of $25, do you want to proceed with the payment? y / n: ')
                if payment_1 != 'y' and payment_1 != 'n':
                    print('You seleccted the wrong option, please try again')
                elif payment_1 == 'y':
                    print(f'\nPayment date: {actual_date} \nYour next payment will be: {one_month_later} ')
                elif payment_1 == 'n':
                    print('See you next time!')
                    time.sleep(2)
            elif payment == '2':
                payment_2 = input(f'You have selected option #2: The gym and yoga is included, for the amount of $35, do you want to proceed with the payment? y / n: ')
                if payment_2 != 'y' and payment_2 != 'n':
                    print('You seleccted the wrong option, please try again')
                elif payment_2 == 'y':
                    print(f'\nPayment date: {actual_date} \nYour next payment will be: {one_month_later} ')
                elif payment_2 == 'n':
                    print('See you next time!')
                    time.sleep(2)
            elif payment == '3':
                payment_3 = input(f'You have selected option #3: The gym, yoga, spinning and nutricionist are included, for the amount of $35, do you want to proceed with the payment? y / n: ')
                if payment_3 != 'y' and payment_3 != 'n':
                    print('You seleccted the wrong option, please try again')
                elif payment_3 == 'y':
                    print(f'\nPayment date: {actual_date} \nYour next payment will be: {one_month_later} ')
                elif payment_3 == 'n':
                    print('See you next time!')
                    time.sleep(2)
        elif menu == '3':
            break

    elif menu == '2':
        class_schedule()
        

# Nutrition and Diet:
# Meal planning
# Food meanings 
    elif menu == '3':
        nutrition = input ('\nYou have selected the option 3, the Nutrition and Diet: \n1->Meal planning \n2->Food meanings \n')
        if nutrition == '0' and nutrition > '3':
            print('You selected the wrong option, please try again')
        elif nutrition == '1':
            meal = input('\nYou have selected meal planning, select how you want to start planning:\n1->Bulk\n2->Cut\n')
            if meal == '0' and meal > '3':
                print('You selected the wrong option, please try again')
            elif meal == '1':
                bulk = ['milk', 'cottage cheese', 'yogurt', 'cheese','kale', 'spinach', 'mustard greens', 'bok choy', 'arugula', 'Swiss chard','Eggs','avocado', 'nut butters', 'plant-based oils']
                print('\nHere you have the best meals when you are bulking: \n')
                for i in bulk:
                    print(i)
                time.sleep(5)
            elif meal == '2':
                cut =  ['lean meat and poultry', 'oily fish', 'eggs','milk', 'yogurt', 'low fat cheese','protein powders such as whey, hemp, rice, and peas', 'beans and pulses']
                print('\nHere you have the best meals when you are cutting')
                for b in cut:
                    print(b)
                time.sleep(5)
        elif nutrition == '2':
            food_meanings = {'Protein': 'Protein Foods include all foods made from seafood; meat, poultry, and eggs; beans, peas, and lentils; and nuts, seeds, and soy products.',     'Carbohydrate': 'Carbohydrates are found in a wide array of both healthy and unhealthy foods—bread, beans, milk, popcorn, potatoes, cookies, spaghetti, soft drinks, corn, and cherry pie. They also come in a variety of forms. The most common and abundant forms are sugars, fibers, and starches.', 'Fluids': 'Glass of plain ole water, milk, Cheers to tart-cherry juice, Cup of tea, Smoothie' }
            food = input('\nif you want to know some importang meanings on the gym, please type:\nProtein\nCarbohydrate\nFluids\n')
            if food != 'Protein' and food != 'Carbohydrate' and food != 'Fluids':
                print('You type wrong one of the options, please try again')
            elif food == 'Protein':
                print(food_meanings['Protein'])
                time.sleep(5)
            elif food == 'Carbohydrate':
                print(food_meanings['Carbohydrate'])
                time.sleep(5)
            elif food == 'Fluids':
                print(food_meanings['Fluids'])
                time.sleep(5)
            more_meanings = input('\nAre you experienced on food Nutrition and Diet and we are missing someting? add more meanins to the dictionary! y/n: ')
            if more_meanings != 'y' and more_meanings != 'n':
                print('You selected the wrong option!')
            elif more_meanings == 'y':
                mean = input('\nPlease add word you will explain: ')
                mean_2 = input(f'\nPlease add here the explanation of {mean}')
                food_meanings.update({mean: mean_2})
                print('\nThis is now the food meanings: ', food_meanings)
                time.sleep(5)


    elif menu == '4':
        print('\nHere you will see your progress tracking, right now, there is no data, so you will need to enter that data based on your weights')
        weight = []
        weights = float(input('\nPlease enter your current weight(Note that the weight will be measure in kg): '))
        workout_training(weight, weights)
        
        
        
        
        


#Trainer ’s name

    elif menu == '5':
        trainers_name = ['Andrey', 'Alejandro', 'Raul', 'Maria', 'Mario']
        print('The trainers available in this gym are: ')
        for i in trainers_name:
            print(i)
        time.sleep(6)


# Gym exercises:

    elif menu == '6':
        exercises = ['Barbell Bentover Rows', 'Dumbbell Split Squats', 'Dumbbell Chest Presses on Swiss Ball', 'Wide-Grip Pullups', 'Dumbbell Step-Ups', 'Medicine Ball Floor Slams', 'Barbell Hip Thrusts', 'Decline Pushups']
        print(f'\nThese are the most popular and favorite excersices at this gym: ')
        for b in exercises:
            print(b)
        time.sleep(5)

        add_excercises = input('\nDo you know a good excersice that we are missing, please add it here!, please confirm if you want to add it; y/n: ')
        if add_excercises != 'y' and add_excercises != 'n':
            print('You selected the wrong option!')

        elif add_excercises == 'y':
            add = input('\nPlease type is the name of the exercise you want to add: ')
            exercises.append(add)
            print('\nYour excersice have been added!')
            for c in exercises:
                print(c)
            time.sleep(5)
    elif menu == '7':
        print(f"Do not be skinny {new_username}!! We'll wait for you!!")
        break