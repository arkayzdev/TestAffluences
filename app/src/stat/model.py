class Data:
    def __init__(self, record_datetime_local, entries, exits, occupancy) -> None:
        self.record_datetime_local = record_datetime_local 
        self.entries = entries
        self.exits = exits
        self.occupancy = occupancy

