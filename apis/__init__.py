from flask_restplus import Api
from core import utils

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

apis = utils.load_apis()
for found_api in apis:
    api.add_namespace(found_api.api)