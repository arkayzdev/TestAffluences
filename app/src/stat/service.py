import pandas as pd
from model import Data

class StatService:
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path


    def get_df_by_id(self, site_id: int, id_column="site_id"):
        df = pd.read_csv(self.data_path)
        df['record_datetime_utc'] = pd.to_datetime(df['record_datetime_utc'])
        return df.loc[df[id_column] == site_id]
    

    def get_df_by_time_range(self, start_datetime: str, end_datetime: str, df, datetime_column="record_datetime_utc"):
        mask = (df[datetime_column] > start_datetime) & (df[datetime_column] < end_datetime)
        new_df = df.loc[mask].copy()
        return new_df
    

    def get_cumulated(df, column_name: str):
        pass

    def convert_sec_to_min(seconds: int):
        return seconds/60
    
    def get_slices(granulate) -> list[dict{"start_time" / "end_time"}]

    def get_data(self, args: dict):
        df = self.get_df_by_id(site_id=args['site_id'])
        new_df = self.get_df_by_time_range(start_datetime=args['start_datetime'], end_datetime=args['end_datetime'])




    

stat = StatService("app/src/stat/data/dataset.csv")
df = stat.get_df_by_id(site_id=2)
new_df = stat.get_df_by_time_range(start_datetime="2024-04-21 23:04:34", end_datetime="2024-04-21 21:47:17", df=df)
print(new_df.head())

