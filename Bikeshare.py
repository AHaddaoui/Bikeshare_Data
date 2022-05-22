import time
import pandas as pd
import numpy as np

# Save csv names
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
    city = input("Please choose the city chicago, new york city or washington: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Incorrect input, please choose City again: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Please choose the month you want: all, january, february, .., june: ").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Incorrect input, please choose Month again: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose the day you want: all, monday, tuesday, ...: ").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday' ,'thursday' ,'friday' ,'saturday' ,'sunday']:
        day = input("Incorrect input, please choose Day again: ").lower()

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
    # based on user input, load city with correct csv name
    df = pd.read_csv(r'{}'.format(CITY_DATA[city]))

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # convert End Time to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract the months and create new column
    df['Month'] = df['Start Time'].dt.month_name()

    # filte by month if the month is not "all"
    if month != 'all':
        # filter by month to create a new df
        df = df[df['Month'] == month.title()]

    # extract the months and create new column
    df['Day'] = df['Start Time'].dt.day_name()

    # filter by day
    if day != 'all':
        # filter by day to create a new df
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most frequent month of travel is: ", df['Month'].value_counts().idxmax())

    # display the most common day of week
    print("The most frequent day of travel is: ", df['Day'].value_counts().idxmax())

    #  extract the hour and create new column
    df['Hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    print("The most frequent starting hour is: ", df['Hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Stations Journey'] = df['Start Station'] + " - " + df['End Station']
    print("Most frequent combination of start station and end station trip: ", df['Stations Journey'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time (mins): ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time (mins): ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('The count of user types is:\n', counts_of_user_types)

    if city != 'washington':
        
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\nThe count of gender:\n', gender_count)

        # Display earliest, most recent, and most common year of birth
        most_common_year_birth = df['Birth Year'].mode()[0]
        print("\nThe most common year of birth is:\n", most_common_year_birth)

        earliest_year_birth = df['Birth Year'].min()
        print("\nThe earliest year of birth is:\n", earliest_year_birth)

        recent_year_birth = df['Birth Year'].max()
        print("\nThe most recent year of birth is:\n", recent_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_stats(df):
    """Displays raw statistics of bikeshares."""
    # Ask user if they wish to see raw data
    raw_input = input('Enter "Yes" to see raw data or "No" to skip.\n').lower()
    row_count = 0
    while True:
        if raw_input == 'yes':
            print(df[row_count : row_count + 5])
            row_count += 5
            raw_input = input('Enter "Yes" to see raw data or "No" to skip.\n').lower()
        elif raw_input =='no':
            break
        else:
            print('Wrong Value, please enter "Yes" or "No" to display raw text.')
            raw_input = input('Enter "Yes" to see raw data or "No" to skip.\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()