# Import Library
import pandas as pd
import weather_anaylsis
import matplotlib.pyplot as plt

# Import Excel File
df = pd.read_excel('SD_year_temp.xlsx')

# Define data variables
month = df['Month']
date_month = df['Date of month']
date_year = df['Date of Year']
max_temp = df['Maximum Temperature']
min_temp = df['Minimum Temperature']
avg_temp = df['Average Temperature']
rain = df['Precipitation']

# interactive menu (code concept borrowed from a youtube video)
# reference:https://www.youtube.com/watch?v=kGY9n5H6nr0&list=WL&index=33&t=1s
loop = 1

while loop == 1:
    # Greeting and options
    print()
    print('Hi! Welcome to the San Diego Weather Report ! :)')
    print("Your options are:")
    print()
    print("1) View by a specific Day in the year of 2019")
    print("2) View by a specific Range of Months in the year of 2019")
    print("3) View by the entire year of 2019")
    print("4) Exit :( ")
    print()
    choice = input("Choose your option: ")
    choice = int(choice)

    # option 1: weather condition on the desired date
    if choice == 1:
        # Input month, then extract the data from the dataframe
        choice_month = input("Please choose a month (1-12): ")
        choice_month = int(choice_month)
        # Make sure the input number is reasonable
        if choice_month < 0 or choice_month > 12:
            print('Please enter a value from 1 to 12')
        else:
            # Input date, then extract the data from the dataframe
            choice_day = input("Please choose a day (1-30/31)" +
                               "[2019 Feduary only up to 28 days]: ")
            choice_day = int(choice_day)
            # Make sure the input number is reasonable
            if choice_day < 0 or choice_day > 31:
                print('Please choose a day (1-30/31)\
                [2019 Feduary only up to 28 days]')
            else:
                choice_month = int(choice_month)
                choice_day = int(choice_day)
                print()
                # Plot out the weather conditon plots
                weather_anaylsis.day_weather(choice_month, choice_day,
                                             month, date_month, max_temp,
                                             min_temp, avg_temp, rain)

    # option 2: weather condition on the desired range of months
    elif choice == 2:
        # Input range of month, then extract the data from the dataframe
        choice_month_start = input("Please choose a start month (1-12): ")
        choice_month_start = int(choice_month_start)
        # Make sure the input number is reasonable
        if choice_month_start < 0 or choice_month_start > 12:
            print('Please reenter a value from 1 to 12')
        else:
            # Input range of month, then extract the data from the dataframe
            choice_month_end = input("Please choose a end month(1-12)," +
                                     "but no less than start month: ")
            choice_month_end = int(choice_month_end)
            # Make sure the input number is reasonable
            if choice_month_end < 0 or choice_month_end > 12\
               or choice_month_end < choice_month_start:
                print("Please reenter a value from 1 to 12 and ",
                      "no less than start month?")
            else:
                choice_month_start = int(choice_month_start)
                choice_month_end = int(choice_month_end)
                # Form a new dataframe with the extracted data set
                df1 = weather_anaylsis.desire_months(choice_month_start,
                                                     choice_month_end, month,
                                                     date_month, date_year,
                                                     max_temp, min_temp,
                                                     avg_temp, rain)
                # Rename the parameters with the new dataframe
                month1 = df1['Month']
                date_month1 = df1['Day']
                date_year1 = df1['Day in Year']
                max_temp1 = df1['Maximum Temperature']
                min_temp1 = df1['Minimum Temperature']
                avg_temp1 = df1['Average Temperature']
                rain1 = df1['Precipitation']
                # Plot out the weather conditon plots
                weather_anaylsis.month_weather(choice_month_start,
                                               choice_month_end, date_year1,
                                               max_temp1, min_temp1,
                                               avg_temp1, rain1)
                plt.show()

    # option 3: weather condition in the year of 2019
    elif choice == 3:
        # Plot out the weather conditon plots
        weather_anaylsis.year_weather(max_temp, min_temp, avg_temp, rain)

        plt.show()

    # option 4: Exit the interactive menu
    elif choice == 4:
        print('Bye Bye :(')
        loop = 0
    # Make sure if the option number is input correctly
    else:
        print('Please enter a value from 1 to 4 !!!!')