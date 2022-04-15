import time
import pandas as pd
import numpy as np

"""Please note that the CSV files are mandatory in order to run the program"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """
    *************************************************************************************************
    User Input 1 get user input for the *city* variable (chicago, new york city, washington).
    Handle invalid user input and give feedback and confirmation to the user.
    """
    cities = ['Chicago','New York','Washington'] #Check, only valid cities allowed!

    city = str(input('Would you like to see data for Chicago, New York, or Washington?\n').title())

    while city not in cities:
        city =input("Please choose only Chicago, New York or Washington!\n").title()

    print("Your choice: {}! If this is not true, please restart the program!\n\n\n".format(city))
    city = city.lower()
    """
    *************************************************************************************************
    User Input 2 get user input for the *timeframe* variable (month, day, none).
    Handle invalid user input and give feedback and confirmation to the user.
    """
    # get user input for timeframe on which to do data analysis
    timeframes = ['Month','Day','None'] #Check, only valid timeframes allowed!

    timeframe = str(input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter\n').title())

    while timeframe not in timeframes:
        timeframe =input('Please choose only "month", "day", or "none"!\n').title()
    print("Your choice: Filter by {0}! OK, the program will filter by {0}!\n\n\n".format(timeframe))
    timeframe = timeframe.lower()

    """
    Case user choise for city +  month filter + NO day filter
    """
    if timeframe == 'month':
        day = 'all' #No day filter will be applied but only month
        """
        *************************************************************************************************
        User Input 3 get user input for the *month* variable (January - June).
        Handle invalid user input and give feedback and confirmation to the user.
        """
        # get user input for month (all, january, february, ... , june)
        months = ['January','February','March','April','May','June',] #Check, only valid month allowed!

        month = str(input('Which month - January, February, March, April, May, or June?\n').title())

        while month not in months:
            month =input('Please choose only "January", "February", "March", "April", "May", or "June"!\n').title()
        print("Your choice: Filter by {0}! OK, the program will now load the data for {0}!\n\n\n".format(month))
        month = month.lower()
        """
        *************************************************************************************************
        Case user choise for city + NO month filter + day filter
        """
    elif timeframe == 'day':
        month = 'all' #No month filter will be applied but only day
        """
        *************************************************************************************************
        User Input 4 get user input for the *day* variable (Monday - Sunday).
        Handle invalid user input and give feedback and confirmation to the user.
        """
        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','all'] #Check, only valid month allowed!

        day = str(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n').title())
        while day not in days:
            day =input('Please choose only "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" or "all"!\n').title()
        print("Your choice: Filter by {0}! OK, the program will now load the data for {0}!\n\n\n".format(day))
        day = day.lower()
        """
        *************************************************************************************************
        Case user choise for city + NO month filter + NO day filter
        """
    else:
        month = 'all' #No month filter will be applied
        day = 'all'   #No day filter will be applied
        print('Due to your choise {}, no time filter will be applied and the program will now load the data!'.format(timeframe))
    """
    *************************************************************************************************
        Closing and return variables city, month , day
    """
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # extract day from the Start Time column to create an day_of_week column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # calculate some first statistics and the process times for this task
    print('Loading the dataset and filter for {}...'.format(city.title()))
    #print('Month filter:', month.capitalize(),'\nDay filter:',day.capitalize())
    print('Month filter:', month.title(),'\nDay filter:',day.title())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # Randomly selected data for the first six months of 2017 are provided for all three cities.
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode() [0]
    print('Most common month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode() [0]
    print('Most common day of week:', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode() [0]
    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode() [0]
    start_count = df['Start Station'].value_counts() [popular_start_station]
    print('Most commonly used start station:', popular_start_station,'with a count of',start_count,'\n')

    value_count_start = df['Start Station'].value_counts()
    print(value_count_start,'\n')
    print('*'*40)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode() [0]
    end_count = df['End Station'].value_counts() [popular_end_station]
    print('Most commonly used end station:', popular_end_station,'with a count of',end_count,'\n')

    value_count_end = df['End Station'].value_counts()
    print(value_count_end,'\n')
    print('*'*40)

    # display most frequent combination of start station and end station trip
    df['trips'] = df['Start Station'] + df['End Station']
    popular_trip = df['trips'].mode() [0]
    popular_trip_count = df['trips'].value_counts() [popular_trip]
    print('Most popular trip:',popular_trip,'with a count of',popular_trip_count,'\n' )

    value_count_trip = df['trips'].value_counts()
    print(value_count_trip,'\n')
    print('*'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    total_travel_hours = ((total_travel/60)/60).round(2)
    print('Total travel time:', total_travel_hours,'hours \n')

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mean_travel_minutes = round((mean_travel/60),2)
    print('Mean travel time:', mean_travel_minutes,'minutes \n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Counts of user types:\n',count_user_type,'\n')

    #As Gender and Birth Year is not provided in all raw datasets a contol point is required.
    #If If user choose Washington as city, then this control point should skip Gender and Birth Year analyses.

    #Control Point for Gender analysis
    try:
        count_gender = df['Gender'].value_counts()
        print('Counts of gender:\n',count_gender,'\n')

    except KeyError:
        print("Sorry, but the Gender statistics cannot be calculated due to missing data in raw dataset!")
        print("The program will therefore skip the Gender analysis and continue with Birth Year analysis...\n")
        # Display earliest, most recent, and most common year of birth

    try:
        #Control Point for Birth Year analysis
        earliest_year_of_birth = df['Birth Year'].min()
        print('Earliest year of birth:\n',int(earliest_year_of_birth),'\n')

        most_recent_year_of_birth = df['Birth Year'].max()
        print('Most recent year of birth:\n',int(most_recent_year_of_birth),'\n')

        most_common_year_of_birth = df['Birth Year'].mode() [0]
        print('Most common year of birth:\n',int(most_common_year_of_birth),'\n')

    except KeyError:
        print("Sorry, but the Birth Year statistics cannot be calculated due to missing data from raw dataset!")
        print("The program will therefore skip the Birth Year analysis!\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    yes_no = ['no','yes'] #Check, only valid choise allowed!

    view_data = str(input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower())

    while (view_data not in yes_no):
        view_data =str(input('Please choose only "yes" or "no"!\n').lower())

    start_loc = 5
    next_loc = 0
    while (view_data != 'no'):
        print(df.iloc[next_loc:start_loc])
        start_loc += 5
        next_loc += 5
        view_data = str(input("Do you wish to continue? Enter yes or no !\n ").lower())

        while (view_data not in yes_no):
            view_data =str(input('Please choose only "yes" or "no"!\n').lower())

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #Displaying summary of dataset and announcing start of calculation
        print(df)
        print('Calculation of statistics started...\n')
        #Calculate statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

""" Comments to Udacity during transmission:
1. I have updated the get_filter function to improve the user interaction. Now the user is also allowed to make some format errors ( e.g. ChiCago) as long as the city has no typos the programm will progress accordingly.

2. I have implemented Control Points in the user_stats function to handle missing raw data e.g. as this is the case for washington.py (gender and birth year missing)

3. I have created the new unction display_data which is allowing to display raw data in chuncs of 5 rows. The function is including checks and user interaction and called in the main program.
"""
