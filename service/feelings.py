from functools import lru_cache
from typing import Dict, Any, Optional, Union, List
import yaml


class FeelingNotFound(Exception):
    pass


@lru_cache
def load_yaml(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as fp:
        return yaml.safe_load(stream=fp)


def get_feelings() -> dict:
    return load_yaml("model/feelings.yaml")["feelings"]


FEELINGS = get_feelings()


def search_multilevel_dict(data: Dict[str, Any], name: str) -> Optional[Union[str, Dict[str, Any]]]:
    """Recursively searches through a multi-level dictionary for the given key."""
    for key, value in data.items():
        if key == name:
            return value
        elif isinstance(value, dict):  # If value is a nested dictionary, search recursively
            result = search_multilevel_dict(value, name)
            if result is not None:  # If found in the nested dict, return the result
                return result
    return None


def get_sub_feelings(name: str) -> Union[str, List[str]]:
    name = name.lower().strip()
    result = search_multilevel_dict(data=FEELINGS, name=name)
    if result is None:
        raise FeelingNotFound
    elif isinstance(result, dict):
        return list(result.keys())
    else:
        return result
