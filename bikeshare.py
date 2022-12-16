import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
    while city not in CITY_DATA.keys():
        city = input('Invalid input! Please enter either chicago, new york city or washington.\n\n').lower()


    print('\nLooks like you want to hear about', city.title(),'!\n')

    # get user input for month (all, january, february, ... , june)
    month = input('Now let\'s specify a month to filter by, or enter "all" to apply no month filter.\n').title()
    while month not in ('All','January', 'February', 'March', 'April', 'May', 'June'):
        month = input('Invalid input! you must enter a month from January - June. Kindly try again.\n\n').title()


    print('\nExcellent! We\'ll make sure to filter by', month,'!\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Now let\'s specify a day of week to filter by, please type abbreviated day name(i.e Mon, Tues) or enter "all" to apply no day filter.\n').title()
    while day not in ('All' , 'Mon' , 'Tues' , 'Wed' , 'Thurs' , 'Fri' , 'Sat' , 'Sun'):
        day = input('Invalid input! you must enter a day from Mon - Sun. Kindly try again.\n\n').title()


    print('\nGreat! We\'ll make sure to filter by', day,'!\n')

    print('\nJust one moment .. Loading the data\n')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'All':
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        df = df[df['Day of Week'] == day.title()]

    print('\nData loaded, Now let\'s apply filters.. this will be done in no time!\n')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nWhat is the most popular month for traveling?\n', df['Month'].mode()[0])

    # display the most common day of week
    print('\nWhat is the most popular day for traveling?\n', df['Day of Week'].mode()[0])

    # display the most common start hour
    print('\nWhat is the most popular hour of the day to start your travels?\n', df['Hour'].mode()[0])
    #hr = df['Hour'].mode()[0]
    #if hr <= 12:
     #   print('\nMost common start hour is: {} AM'.format(hr))
    #else:
     #   print('\nMost common start hour is: {} PM'.format(hr%12))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    start_end_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)
    print('The most frequent combination of start and end station trip is:\n', start_end_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ' , total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: ' , mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nWhat is the breakdown of users?\n', df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('\nWhat is the breakdown of gender?\n', df['Gender'].value_counts())
    except:
        print('\nNo gender data to share.')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nWhat is the oldest, youngest, and most popular year of birth, respectivly?\n', earliest_birth_year,',', recent_birth_year,',', common_birth_year )
    except:
        print('\nNo Birth year data to share.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(city):
    df = pd.read_csv(CITY_DATA[city])
    user_input = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while user_input == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?\n").lower()
        if view_data == 'no':
            break
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
