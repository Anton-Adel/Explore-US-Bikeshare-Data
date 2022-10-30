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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
         city=input('please int the city name you looking for (chicago, new york city, washington): \n').lower()
         if(city.lower() in ('chicago','new york city','washington')):
            break
         else:
            print('Enter valid input')
            continue
   
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
         month=input('please enter the month you want to filter with (january, february, ... , june) or enter all for no filter: \n').title()
            
         if(month in ('January', 'February', 'March', 'April', 'May', 'June', 'All')):
            break
         else:
            print('Enter valid input')
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    while True:
         day=input('please enter the day you want to filter with (monday, tuesday, ... sunday)or enter all for no filter: \n').title()
            
         if(day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All')):
            break;
         else:
            print('Enter valid input')
            continue    

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print(df.head())
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month_ = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_]
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
        


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month: ',df['month'].mode()[0])


    # TO DO: display the most common day of week
    print('most common day of week: ',df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    print('the most common start hour: ',df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station: ',df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print('most commonly used end station: ',df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    combination=df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip: ',df['Start Station'].value_counts().idxmax()," & ",df['End Station'].value_counts().idxmax())
  # print(df[['End Station','End Station']].max())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ',(df['Trip Duration'].sum())/86400,' day')


    # TO DO: display mean travel time
    print('total travel time: ',(df['Trip Duration'].mean())/3600,' hour')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types: ',df.groupby(['User Type'])['User Type'].count())


    # TO DO: Display counts of gender
    if city != 'washington':
        print('counts of gender: ',df.groupby(['Gender'])['Gender'].count())
        print('earliest, most recent, and most common year of birth: ',df['Birth Year'].min()," ", df['Birth Year'].max()," ",df['Birth Year'].value_counts().idxmax())
    
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    

    # TO DO: Display earliest, most recent, and most common year of birth
   
   
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        start_loc = 0
        while (view_data=='yes'):
           print(df.iloc[start_loc:start_loc+5])
           start_loc += 5
           view_data = input("Do you wish to continue?: ").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
