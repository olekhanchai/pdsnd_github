import time
import pandas as pd
import numpy as np

#Cities can be add more below.
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 0
    month = ""
    day = ""
    while city not in (range(1, 4)):
        print("Please input city name");
        idx = 1
        for x in CITY_DATA.keys():
            print("{0}:{1}".format(idx, x))
            idx = idx + 1
            
        city = int(input())

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in ('all', '1', '2', '3', '5', '6'):
        print("Please input number of month for filter\n")
        print("'1:january', '2:february', '3:march', '5:may', '6:june' or 'all' for no filter) : ")
        month = str(input())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in ('all', '0', '1', '2', '3', '4', '5', '6'):
        print("Please input number of day of week\n")
        print("'0:monday', '1:tuesday', '2:wednesday', '3:thursday', '4:friday', '5:saturday', '6:sunday' or 'all' for no filter) : ")
        day = str(input())

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
            
    df = pd.read_csv(list(CITY_DATA.values())[int(city)-1])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month'] = df['Start Time'].dt.month
    df['DOW'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        df = df[(df['Month'] == int(month))]
    
    if day != 'all':
        df = df[(df['DOW'] == int(day))]
                             
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month : {0}'.format(df['Start Time'].dt.month.mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of week : {0}'.format(df['Start Time'].dt.day_name().mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour : {0}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    display_data(df)
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station : ')
    most_start = df['Start Station'].mode()[0]
    print(most_start)

    # TO DO: display most commonly used end station
    print('Most commonly used end station : ')
    most_end = df['End Station'].mode()[0]
    print(most_end)

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip : ')
    print(most_start+most_end)
                             
    print("\nThis took %s seconds." % (time.time() - start_time))
    display_data(df)
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time : {0:.2f}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time {0:.2f}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    display_data(df)
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types : ')
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns and 'Birth Year' in df.columns:    
        # TO DO: Display counts of gender
        print('Counts of gender : ')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Most earliest year of birth : {0:.0f}'.format(df['Birth Year'].min()))

        print('Most recent year of birth : {0:.0f}'.format(df['Birth Year'].max()))

        print('Most common year of birth : {0:.0f}'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display dataframe 5 items from input"""
    
    ans = input('Would you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    #Prevent display overflow data
    while (ans.lower() == "yes" and start_loc <= df.count()[0]):
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        ans = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
