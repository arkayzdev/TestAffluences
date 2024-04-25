from flask_restful import Resource, reqparse, inputs, abort
from occupancy.service import OccupancyService
from flask import jsonify
from occupancy.exception import *


class OccupancyCheckArgs:

    pattern = {'datetime': r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'}
    
    def get_occupancy_args(self) -> dict:
        parser = reqparse.RequestParser()
        parser.add_argument('site_id', type=int, required=True, help="Invalid or missing parameter 'site_id'")
        parser.add_argument('start_datetime', type=inputs.regex(self.pattern['datetime']), required=True, help="Invalid or missing parameter 'start_datetime'")
        parser.add_argument('end_datetime', type=inputs.regex(self.pattern['datetime']), required=True, help="Invalid or missing parameter 'end_datetime'")
        parser.add_argument('granularity', type=int, required=True, help="Invalid or missing parameter 'granularity'")

        args = parser.parse_args(strict=True)
        return args


class OccupancyListController(Resource):
    def __init__(self) -> None:
        self.check_args = OccupancyCheckArgs()
        self.occupancy_service = OccupancyService()
    

    def get(self):
        try:
            args = self.check_args.get_occupancy_args()
            data = self.occupancy_service.get_data(args)
            response = {
                'site_id': args['site_id'],
                'data' : [_data.json() for _data in data]
            }
            return jsonify(response)
        except SiteIdNotFoundException as e:
           abort(http_status_code=404, message=str(e))
        except DatetimeRangeNotFoundException as e:
            abort(http_status_code=404, message=str(e))
        except EntriesExitsAccessException as e:
            abort(http_status_code=500, message=str(e))
        except DatetimeSlicesException as e:
            abort(http_status_code=500, message=str(e))
        except OccupancyException as e:
            abort(http_status_code=500, message=str(e))
        

   