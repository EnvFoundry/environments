"""Validate the environment directory and its stable identifiers."""

import json
from pathlib import Path

from jsonschema import Draft202012Validator


def main():
    root = Path(__file__).resolve().parent
    schema = json.loads((root / "catalog.schema.json").read_text(encoding="utf-8"))
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(catalog)
    ids = [entry["id"] for entry in catalog["environments"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Environment IDs must be unique")
    print(f"Catalogue valid: {len(ids)} environments")


if __name__ == "__main__":
    main()
