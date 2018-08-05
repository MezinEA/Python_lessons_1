import json

class Builder:
    def __init__(self, my_data):
        for key, val in my_data.items():
            setattr(self, key, val)


first_json = '{"key" : "Val", "key3" : "Val3", }'
second_json = '{"key2" : "Val2"}'

first_obj = Builder(json.detect_encoding(first_json))