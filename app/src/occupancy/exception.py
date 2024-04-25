class SiteIdNotFoundException(Exception):
    def __init__(self, site_id: int) -> None:
        self.site_id = site_id

    def __str__(self) -> str:
        return f"Site with id '{self.site_id}' not found."
    
class DatetimeRangeNotFoundException(Exception):
    def __init__(self, start_datetime: str, end_datetime: str) -> None:
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def __str__(self) -> str:
        return f"Data with datetime range '{self.start_datetime}' - '{self.start_endtime}' not found."
    

class EntriesExitsAccessException(Exception):
    def __init__(self, start_datetime: str, end_datetime: str) -> None:
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def __str__(self) -> str:
        return f"Erreur while getting entries and exits in datetime range '{self.start_datetime}' - '{self.start_endtime}'."
    

class DatetimeSlicesException(Exception):
    def __init__(self, start_datetime: str, end_datetime: str, granularity: int) -> None:
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.granularity = granularity
        
    def __str__(self) -> str:
        return f"Erreur while getting slices in datetime range '{self.start_datetime}' - '{self.start_endtime}' with granularity '{self.granularity}'."
 
    
class OccupancyException(Exception):
    def __init__(self, cumulated_entries: int, cumulated_exits: int) -> None:
        self.cumulated_entries = cumulated_entries
        self.cumulated_exits = cumulated_exits

    def __str__(self) -> str:
          return f"Erreur while calculating occupancy with cumulated entried '{self.cumulated_entries}' and cumulated exits '{self.cumulated_exits}'."
    