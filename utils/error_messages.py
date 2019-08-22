import json

error_message = lambda val: {
    "status"      : 400,
    "content"     : json.dumps({"message":val, "error": "Bad request"}),
    "content_type": "application/json"
}

not_found_message = lambda val : {
    "content"     : json.dumps({"message": val, "error": "Not found"}),
    "content_type": "application/json"
}