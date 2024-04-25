class SampleAccessDbException(Exception):
    def __init__(self, sample_id: int, method: str) -> None:
        self.sample_id = sample_id
        self.method = method

    def __str__(self) -> str:
        if self.sample_id:
            return f"Error {self.method} sample '{self.sample_id}'."
        else: 
            return f"Error {self.method} samples."
        

class SampleIdNotFoundException(Exception):
    def __init__(self, sample_id: int) -> None:
        self.sample_id = sample_id

    def __str__(self) -> str:
        return f"Sample with id '{self.sample_id}' not found."