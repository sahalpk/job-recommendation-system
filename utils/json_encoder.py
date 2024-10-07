from flask.json import JSONEncoder
from bson import ObjectId
from models.jobs import Job

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Job):
            return obj.to_dict()
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)