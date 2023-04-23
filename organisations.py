
from typing import Dict, List, Optional, Union
from pymongo.collection import Collection
from models import Organisation

def create_organisation(org: Organisation, organisations_collection: Collection) -> Organisation:
    org_dict = org.dict()
    result = organisations_collection.insert_one(org_dict)
    org_dict['_id'] = str(result.inserted_id)
    return Organisation(**org_dict)

def list_organisations(name: Optional[str], limit: int, offset: int, organisations_collection: Collection) -> Dict[str, Union[int, List[Organisation]]]:
    query = {}
    if name:
        query['name'] = {'$regex': name}
    organisations = organisations_collection.find(query).skip(offset).limit(limit)
    total_count = organisations_collection.count_documents(query)
    return {'total_count': total_count, 'organisations': [Organisation(**o) for o in organisations]}
