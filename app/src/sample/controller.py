from flask_restful import Resource, reqparse, inputs, abort
from sample.service import SampleService
from sample.exception import SampleIdNotFoundException, SampleAccessDbException
from flask import jsonify

class SampleCheckArgs:

    # pattern = {'name' : r'\b[A-Za-zÀ-ÖØ-öø-ÿ\-]{1,50}\b'}
    
    def get_sample_args(self) -> dict:
        parser = reqparse.RequestParser()
        # parser.add_argument('name', type=inputs.regex(self.pattern['name']), required=True, help="Invalid or missing parameter 'name'")
        # parser.add_argument('description', type=str, required=True, help="Invalid or missing parameter 'description'")
        args = parser.parse_args(strict=True)
        return args


class SampleController(Resource):

    def __init__(self) -> None:
        self.check_args = SampleCheckArgs()
        self.sample_service = SampleService()


    def get(self, sample_id: int):
        try:
            sample = self.sample_service.select_one_by_id(sample_id=sample_id)
            return jsonify(sample.json())
        except SampleIdNotFoundException as e:
            abort(http_status_code=404, message=str(e))
        except SampleAccessDbException as e:
            abort(http_status_code=500, message=str(e))
   

    def put(self, sample_id: int):
        try:
            args = self.check_args.get_sample_args()
            self.sample_service.update(sample_id=sample_id, args=args)
            return jsonify({'message': f"Sample '{sample_id}' successfully updated."})
        except SampleIdNotFoundException as e:
            abort(http_status_code=404, message=str(e))
        except SampleAccessDbException as e:
            abort(http_status_code=500, message=str(e))        
   

    def delete(self, sample_id: int):
        try:
            self.sample_service.delete(sample_id=sample_id)
            return jsonify({'message': f"Sample '{sample_id}' successfully deleted."})
        except SampleIdNotFoundException as e:
            abort(http_status_code=404, message=str(e))
        except SampleAccessDbException as e:
            abort(http_status_code=500, message=str(e)) 
            
   
    
class SampleListController(Resource):
    def __init__(self) -> None:
        self.check_args = SampleCheckArgs()
        self.sample_service = SampleService()
    

    def get(self):
        try:
            categories = self.sample_service.select_all()
            if categories:
                return jsonify([sample.json() for sample in categories])
            else:
                return jsonify({'message': "No sample found."})
        except SampleAccessDbException as e:
            abort(http_status_code=500, message=str(e))
        

    def post(self):
        try:
            args = self.check_args.get_sample_args()
            self.sample_service.insert(args=args)
            return jsonify({'message': f"Sample '{args['name']}' successfully created."})
        except SampleAccessDbException as e:
            abort(http_status_code=500, message=str(e))