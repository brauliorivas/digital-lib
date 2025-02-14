import os
import json


class Loader:
    def __init__(self, file_name, schema):
        self.file_name = file_name
        self.schema = schema

    def load(self):
        if not os.path.isfile(self.file_name):
            schema_file = open(self.file_name, "w")
            schema_file.write("[]")
            schema_file.close()

        with open(self.file_name, "r+") as schema_file:
            schema_file = json.load(schema_file)

        entities = []
        for entity in schema_file:
            entities.append(self.schema.from_dict(entity))

        return entities

    def save(self, entities):
        entities_dict = []
        for entity in entities:
            entity_dict = self.schema.to_dict(entity)
            entities_dict.append(entity_dict)

        with open(self.file_name, "w") as entities_file:
            entities_file.write(json.dumps(entities_dict))
