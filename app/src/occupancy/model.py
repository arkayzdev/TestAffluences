class Data:
    def __init__(self, record_datetime_local: str, entries: int, exits: int, 
                 occupancy: int, cumulated_entries: int, cumulated_exits: int) -> None:
        self.record_datetime_local = record_datetime_local 
        self.entries = entries
        self.exits = exits
        self.cumulated_entries = cumulated_entries
        self.cumulated_exits = cumulated_exits
        self.occupancy = occupancy

    def json(self):
        return {
            "record_datetime_local": self.record_datetime_local.strftime("%Y-%m-%d %H:%M:%S"),
            "entries" : self.entries,
            "exits" : self.exits,
            "cumulated_entries" : self.cumulated_entries,
            "cumulated_exits" : self.cumulated_exits,
            "occupancy" : self.occupancy
        }