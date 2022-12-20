import pandas as pd


def to_dataframe(year):
    '''csv to DataFrame'''
    file_name = f'CrimeData-{year}.csv'
    df = pd.read_csv(file_name, header=0)
    df = reformat_date(df)
    df = reformat_time(df)
    return df


def drop_by_date(df):
    '''drop all rows with OccurDate before 2018'''
    df = df.loc[(df['OccurDate'] >= '2018-01-01')]
    return df


def reformat_date(df):
    '''reformat OccurDate column from slashes to dashes'''
    for index, date in df.OccurDate.items():
        date = date.replace('/', '-')
        date = add_zeros(date)
        df.at[index, 'OccurDate'] = date
    return df


def add_zeros(date):
    '''add zeros if necessary to date'''
    x = date.split('-')
    date = ''
    year = x[2]
    date += year + '-'
    month = x[0]
    month = month + '-'
    day = x[1]
    if len(month) == 2:
        month = '0' + month
        date += month
    else:
        date += month
    if len(day) == 1:
        day = '0' + day
        date += day
    else:
        date += day
    return date


def reformat_time(df):
    '''reformat time from military to standard 12-hour clock'''
    for index, mil_time in df.OccurTime.items():
        mil_time = str(mil_time)
        if len(mil_time) == 4:
            hour = mil_time[:2]
            minutes = mil_time[2:]
            if int(hour) < 12:
                time = f'{hour}:{minutes} AM'
                df.at[index, 'OccurTime'] = time
            elif int(hour) == 12:
                time = f'{hour}:{minutes} PM'
                df.at[index, 'OccurTime'] = time
            else:
                hour = str(int(hour) - 12)
                time = f'{hour}:{minutes} PM'
                df.at[index, 'OccurTime'] = time
        if len(mil_time) == 3:
            hour = mil_time[:1]
            minutes = mil_time[1:]
            time = f'{hour}:{minutes} AM'
            df.at[index, 'OccurTime'] = time
        if len(mil_time) == 2:
            time = f'12:{mil_time} AM'
            df.at[index, 'OccurTime'] = time
    return df


def change_neighborhood(df):
    '''replace neighborhood names to match Portland Maps GeoJSON MapLabels'''
    df['Neighborhood'] = df['Neighborhood'].replace('Old Town/Chinatown', 'Old Town')
    df['Neighborhood'] = df['Neighborhood'].replace('Northwest', 'Northwest District')
    df['Neighborhood'] = df['Neighborhood'].replace(['Buckman East', 'Buckman West'], 'Buckman')
    return df

    # neighborhood names to change:
        # Northwest to Northwest Disctrict
        # Old Town/Chinatown to Old Town
        # Buckman East to Buckman
        # Buckman West to Buckman

def main():
    # list of years for dataframe
    years = [2018, 2019, 2020, 2021, 2022]

    # empty list for dataframes
    frames = []

    # make dataframes for each year and append to frames list
    for year in years:
        df = to_dataframe(year)
        frames.append(df)

    # join dataframes into one dataframe
    df = pd.concat(frames)

    # drop columns OpenDataX and OpenDataY
    df.drop(columns=['OpenDataX', 'OpenDataY'])

    # drop rows with OccurDate before 2018
    df = drop_by_date(df)

    # replace neighborhood names
    df = change_neighborhood(df)

    # dataframe to csv for tableau
    df.to_csv('crime_data.csv')



if __name__ == '__main__':
    main()