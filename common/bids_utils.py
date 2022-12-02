import json
import os
import pathlib as pl
from typing import Dict, List


def remove_all_file_extensions(file_path: str):
    file_path = pl.Path(file_path)
    stem = file_path.stem.split('.', maxsplit=1)[0]
    return (file_path.parent / stem).as_posix()


def get_all_file_extensions(file_path: str):
    file_path = pl.Path(file_path)
    stem = file_path.name
    if '.' in stem:
        return stem.split('.', maxsplit=1)[1]
    return stem


def bids_file_to_dict(file_path) -> Dict[str, str]:
    base_path = remove_all_file_extensions(file_path)
    file_path = pl.Path(file_path)
    stem = pl.Path(base_path).stem

    bids_source, bids_remainder = stem.split('_', maxsplit=1)
    bids_tags, bids_suffix = bids_remainder.rsplit('_', maxsplit=1)

    tags = [tuple(tag.split('-', maxsplit=1)) if '-' in tag else (tag, 'True') for tag in bids_tags.split('_')]
    bids_dict = {k: v for k, v in tags}
    bids_dict['_source'] = bids_source
    bids_dict['_suffix'] = bids_suffix
    bids_dict['_filepath'] = file_path.as_posix()
    return bids_dict


def group_bids_dicts(bids_dicts: List[Dict[str, str]]) -> List[List[Dict[str, str]]]:
    groups_dict: Dict[str, List[Dict[str, str]]] = {}

    for bids_dict in bids_dicts:
        group_id = '_'.join(bids_dict.keys())
        if group_id in groups_dict:
            groups_dict[group_id].append(bids_dict)
        else:
            groups_dict[group_id] = [bids_dict]

    return list(groups_dict.values())


def bids_file_fetch_json(local_path: str):
    json_path = remove_all_file_extensions(local_path) + '.json'
    if not os.path.exists(json_path):
        return None
    with open(json_path, 'r') as file:
        re = json.load(file)
    return re
