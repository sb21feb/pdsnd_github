import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyse.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the name of the city you want to analyze")
        if city not in ('chicago','new york city','washington'):
            print('Try again')
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the name of the month you want to analyze")
        if month not in ('January','February','March','April','May','June','all'):
            print('Try again')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the name of the week you want to analyze")
        if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','all'):
            print('Try again')
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
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
    print('The most common month is ',df['month'].mode())

    # display the most common day of week
    print('The most common day of week is ',df['day_of_week'].mode())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is ',df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Commonly used start station ",df['Start Station'].mode())

    # display most commonly used end station
    print("Most Commonly used end station ",df['End Station'].mode())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is ',sum(df['Trip Duration'])/86400,' days')

    # display mean travel time
    print('Mean travel time is ',(df['Trip Duration'].mean())/60,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of user types is ',df['User Type'].value_counts())

    # Display counts of gender
    print('Count of gender is ',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('Earliest year of birth is ',df['Birth Year'].min())
    print('Most recent year of birth is ',df['Birth Year'].max())
    print('Most common year of birth is ',df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Say yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()