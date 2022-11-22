import pandas as pd
import numpy as np
import json
import pickle

# define list of existing stations
with open("data/stations/station_information.json") as f:
    data = json.load(f)

stations = pd.DataFrame(data['data']['stations'])

# number of stations
nb_stations = len(stations['station_id'].unique())

# match id of station to index
stations_match = dict(zip(stations['station_id'].unique().astype(int),range(nb_stations)))

# for a given month, extract d
def extract_d(month_path):
    trips = pd.read_csv(month_path)

    trips.starttime = trips.starttime.apply(pd.to_datetime)
    trips.stoptime = trips.stoptime.apply(pd.to_datetime)

    trips['start_hour'] = trips.starttime.apply(lambda x: x.hour)
    trips['start_minute'] = trips.starttime.apply(lambda x: x.minute)
    trips['start_day'] = trips.starttime.apply(lambda x: x.day)

    trips['stop_hour'] = trips.stoptime.apply(lambda x: x.hour)
    trips['stop_minute'] = trips.stoptime.apply(lambda x: x.minute)
    trips['stop_day'] = trips.stoptime.apply(lambda x: x.day)

    trips = trips.loc[(trips['start station id'].isin(stations_match.keys())) & (trips['end station id'].isin(stations_match.keys()))]

    # create hourly demand matrix 
    d = np.zeros((nb_stations, nb_stations,max(trips['start_day'])*24))

    # group trips
    grouped_trips = trips.groupby(['start station id','end station id','start_day','start_hour']).size().reset_index(name='count')

    # fill demand matrix
    for i in range(len(grouped_trips)):
        d[stations_match[grouped_trips.iloc[i]['start station id']],stations_match[grouped_trips.iloc[i]['end station id']],(grouped_trips.iloc[i]['start_day']-1)*24+grouped_trips.iloc[i]['start_hour']] = grouped_trips.iloc[i]['count']

    return d

# save in data folder
d = extract_d("data/trips/202210-bluebikes-tripdata.csv")
with open('data/parameters/demand_matrix.pkl','wb') as f:
    pickle.dump(d,f)