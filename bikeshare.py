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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
                print('That\'s not a valid city. Please choose between Chicago, New York City and Washington')
                continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose and enter a month (all, january, february, ... , june): ").lower()
        if month not in months:
            print('That\'s not a valid month. Please choose between all, january, february, ... , june')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Choose and enter a day of week (all, monday, tuesday, ... sunday): ")).lower()
        if day not in days:
            print('That\'s not a valid day of week. Please choose between all, monday, tuesday, ... sunday')
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
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
    df['start_hour'] = df['Start Time'].dt.hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    co_month = df['month'].mode()[0]
    print('Most common month is ', c_month)

    # TO DO: display the most common day of week
    c_day_of_week = df['day_of_week'].mode()[0]
    print('Most common dow is ', c_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_c_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is ', most_c_start_station)
    # TO DO: display most commonly used end station
    most_c_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is ', most_c_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combo = df['comb'].mode()[0]
    print('The most frequent combination of start and end station is ', most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration = df['Trip Duration'].sum()
    print('The total time of travel is {} seconds'.format(duration))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('The mean time of travel is {} seconds'.format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The user type is {}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('The count of genders is {}'.format(gender))
    else:
        print('Gender information is not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]
        print('The earliest birth year is {}'.format(earliest_birth_year))
        print('The most recent birth year is {}'.format(recent_birth_year))
        print('The most common year of birth is {}'.format(common_year_birth))
    else:
        print('Birth year information is not available for this city')

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
