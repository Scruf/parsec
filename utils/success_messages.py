import json

object_create = lambda val: {
    "status"      : 200,
    "content"     : json.dumps({"message":val}),
    "content_type": "application/json"
}

success_message = lambda val: {
    "status"      :200,
    "content"     : json.dumps(val),
    "content_type":"application/json"
}