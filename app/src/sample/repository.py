from sample.model import Sample
from database import db
from app import app
from sample.exception import SampleAccessDbException


class SampleRepo():
    def select_all(self) -> list[Sample]:
        try:
            Samples = Sample.query.all()
            if not Samples:
                return None
            return Samples
        except Exception:
            raise SampleAccessDbException(Sample_id=None, method="getting")
        
    def insert(self, new_sample: Sample) -> None:
        try:
            with app.app_context():
                db.session.add(new_sample)
                db.session.commit()
                db.session.close()
        except Exception:
            raise SampleAccessDbException(sample_id=None, method="creating")
        
    
    def update(self, sample_id: int, update_sample: Sample) -> None:
        try:
            with app.app_context():
                sample = Sample.query.filter_by(id=sample_id).first()
                # sample.name = update_sample.name
                # sample.description = update_sample.description
                db.session.commit()
                db.session.close()
        except Exception:
            raise SampleAccessDbException(sample_id=sample_id, method="updating")


    def delete(self, sample_id: int) -> None:
        try:
            with app.app_context():
                sample = Sample.query.filter_by(id=sample_id).first()
                db.session.delete(sample)
                db.session.commit()
                db.session.close()
        except Exception:
            raise SampleAccessDbException(sample_id=sample_id, method="deleting")