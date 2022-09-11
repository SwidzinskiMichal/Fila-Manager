from jsonschema import validate
import json

def test_valiate():
    with open("schema.json") as f:
        schema = json.load(f)

    with open("config.json") as f:
        config = json.load(f)

    result = validate(instance=config, schema=schema)
    assert result == None
