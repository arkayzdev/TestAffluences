from sample.model import Sample
from sample.repository import SampleRepo
from sample.exception import SampleIdNotFoundException

class SampleService:

    def __init__(self) -> None:
        self.sample_repo = SampleRepo()


    def select_one_by_id(self, sample_id: int):
        sample = self.sample_repo.select_one_by_id(sample_id=sample_id)
        if sample:
            return sample
        else:
            raise SampleIdNotFoundException(sample_id=sample_id)
        

    def select_all(self):
        events = self.sample_repo.select_all()
        return events


    def insert(self, args: dict):
        new_sample = Sample()
        self.sample_repo.insert(new_sample=new_sample)
    

    def update(self, sample_id: int, args: dict):
        update_sample = Sample()
        sample = self.sample_repo.select_one_by_id(sample_id=sample_id)
        
        if not sample:
            raise SampleIdNotFoundException(sample_id=sample_id)
        
        self.sample_repo.update(sample_id=sample_id, update_sample=update_sample)
        
        
    def delete(self, sample_id: str):
        if not self.sample_repo.select_one_by_id(sample_id=sample_id):
            raise SampleIdNotFoundException(sample_id=sample_id)
        self.sample_repo.delete(sample_id=sample_id)