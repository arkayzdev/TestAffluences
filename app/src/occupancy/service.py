import pandas as pd
from occupancy.model import Data
from occupancy.exception import *

class OccupancyService:
    def __init__(self, data_path="assets/dataset.csv") -> None:
        self.data_path = data_path


    def get_df_by_id(self, site_id: int):
        try:
            df = pd.read_csv(self.data_path)
            df['record_datetime_utc'] = pd.to_datetime(df['record_datetime_utc'])
            if df.loc[df["site_id"] == site_id]:
                return df.loc[df["site_id"] == site_id]
            else:
                raise SiteIdNotFoundException(site_id=site_id)
        except:
            raise SiteIdNotFoundException(site_id=site_id)
    

    def get_df_by_time_range(self, start_datetime: str, end_datetime: str, df):
        try:
            mask = (df["record_datetime_utc"] >= start_datetime) & (df["record_datetime_utc"] <= end_datetime)
            new_df = df.loc[mask].copy()
            return new_df
        except:
            raise DatetimeRangeNotFoundException(start_datetime=start_datetime, end_datetime=end_datetime)
        
    

    def get_entries_exits(self, df, start_datetime: str, end_datetime: str) -> dict:
        try:
            new_df = self.get_df_by_time_range(start_datetime=start_datetime, end_datetime=end_datetime, df=df) 
            return new_df[['entries', 'exits']].sum().to_dict()
        except:
             raise EntriesExitsAccessException(start_datetime=start_datetime, end_datetime=end_datetime)
        
    
    def get_datetime_slices(self, start_time: str, end_time:str, granularity: int) :
        try:
            new_start_datetime = pd.to_datetime(start_time, format="%Y-%m-%d %H:%M:%S") - pd.Timedelta(seconds=granularity)
            return pd.date_range(start=new_start_datetime, end=end_time, freq=f"{granularity}s") 
        except:
            raise DatetimeSlicesException(start_datetime=start_time, end_datetime=end_time, granularity=granularity)
    
    
    def get_occupancy(self, cumulated_entries: int, cumulated_exits: int):
        try:
            return cumulated_entries - cumulated_exits
        except:
            raise DatetimeSlicesException(cumulated_entries=cumulated_entries, cumulated_exits=cumulated_exits)
        

    def get_data(self, args: dict):
        data = list()
        datetime_slices = self.get_datetime_slices(start_time=args['start_datetime'], end_time=args['end_datetime'], granularity=args['granularity'])
        df = self.get_df_by_id(args['site_id'])
        for i in range(1, len(datetime_slices)):
            cumulated_entries_exits = self.get_entries_exits(df=df, start_datetime=datetime_slices[0], 
                                                             end_datetime=datetime_slices[i])
            entries_exits = self.get_entries_exits(df=df, start_datetime=datetime_slices[i-1], 
                                                   end_datetime=datetime_slices[i])
            occupancy = self.get_occupancy(cumulated_entries=cumulated_entries_exits['entries'], 
                                           cumulated_exits=cumulated_entries_exits['exits'])
            
            new_data = Data(record_datetime_local=datetime_slices[i], entries=entries_exits['entries'],
                            exits=entries_exits['exits'], occupancy=occupancy, cumulated_entries=cumulated_entries_exits['entries'],
                            cumulated_exits=cumulated_entries_exits['exits'])
            data.append(new_data)
        return data



        


