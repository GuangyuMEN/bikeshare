#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import math
import time
import pandas as pd
import matplotlib.pyplot as plt
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["all", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input(" please choose a city: ").lower()
        if city not in CITY_DATA:
            print("It doesnt in our dataset")
            continue
        else:
            break

    while True:
        month = input(" Please type a month or all for all months: ").lower()
        if month not in months:
            print("It doesnt in our dataset")
            continue
        else:
            break

    while True:
        day = input(" Please type a day of week or all for all days: ").lower()
        if day not in days:
            print("It doesn't in our dataset")
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = months.index(month)
        df = df[df["month"] == month]
    if day != 'all':
        df = df[df["day_of_week"] == day.title()]
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    df["Combination Station"] = df['Start Station'] + df['End Station']
    popular_combination = df['Combination Station'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        df["User Type"].value_counts()
        df["Gender"].value_counts()
        df["Birth Year"].min()
        df["Birth Year"].max()
        df["Birth Year"].mode()
    except KeyError:
        print("There are no user stats in this city")
    else:
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
        print(df.head())
        print("\nThese are the first five lines of data for your request.")
        i = 5
        while i <= df.shape[0]:
            if_more_data = input('\n Do you want more five lines of datas? Enter yes or no.\n')
            if if_more_data.lower() == 'yes':
                print(df[i: i+5])
                i += 5
            else:
                break
        restart = input('\nThere are no more datas.Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




