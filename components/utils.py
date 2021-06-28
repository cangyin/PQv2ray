import os, sys
import re
from os import path
from typing import List, Tuple, Dict, Set, Union, Optional, Iterable
from copy import deepcopy
import functools
import json
import logging
from textwrap import dedent
from traceback import format_exc
import subprocess as subp
import shlex
from shutil import copy as copy_file

import psutil

file_encoding = 'UTF-8'
qv2ray_bin_name = 'qv2ray.exe' if sys.platform == 'win32' else 'qv2ray'


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s][%(module)s:%(lineno)d] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('./log.txt', 'wt', encoding=file_encoding)
    ]
)
logger = logging.getLogger(__name__)


def load_json(file :str):
    return json.loads(read_text_file(file))

def dump_json(obj, file :str):
    write_text_file(file, json.dumps(obj, ensure_ascii=False, indent=4))

def dump_jsons(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4)

@functools.lru_cache(maxsize=None)
def read_text_file(file :str):
    try:
        with open(file, 'rt', encoding=file_encoding) as f:
            return f.read()
    except Exception as e:
        logger.error('Error opening file: \n' + repr(e))
        return ''

def clear_cache():
    read_text_file.cache_clear()

def write_text_file(file :str, text :str, mkdirs :bool=True):
    if mkdirs:
        os.makedirs(path.abspath(path.dirname(file)), exist_ok=True)
    with open(file, 'wt', encoding=file_encoding) as f:
        f.write(text)

def get_repr_mapping(node :'Node', **more):
    d = node.get_format_dict()
    d.update(more)
    # {
    #     "node.id": "udjeisuydjfk",
    #     "node.name": "Lv2. 香港01",
    #     "port": 3001,
    #     
    # }
    return d

def format_repr(repr_str, d :dict) -> str:
    result = repr_str
    for k, v in d.items():
        if '{' + k + '}' == repr_str:
            return v
        else:
            result = result.replace('{' + k + '}', str(v))
    return result

def _format_json_obj(repr_obj, d):
    if isinstance(repr_obj, list):
        return [_format_json_obj(o, d) for o in repr_obj]
    elif isinstance(repr_obj, dict):
        return {format_repr(k, d): _format_json_obj(v, d) for k, v in repr_obj.items()}
    elif isinstance(repr_obj, str):
        return format_repr(repr_obj, d)
    else:
        return repr_obj

def format_json_obj(repr_obj, d):
    return _format_json_obj(deepcopy(repr_obj), d)

def deduplicate(l, key=None):
    if key is None:
        return list(dict.fromkeys(l))
    else:
        keys = (key(i) for i in l)
        d = dict.fromkeys(keys)
        if len(d) != len(l):
            new_l = []
            new_keys = []
            for i in l:
                k = key(i)
                if k not in new_keys:
                    new_l.append(i)
                    new_keys.append(k)
            return new_l
        else:
            return l

def has_duplication(l, key=None) -> bool:
    return len(deduplicate(l), key) != len(l)

def process_exists(name :str):
    return name in (p.name() for p in psutil.process_iter())

def qv2ray_process_exists():
    return process_exists(qv2ray_bin_name)

def start_process(cmd :str):
    subp.Popen(
        args=shlex.split(cmd),
        start_new_session=True,
        creationflags=subp.CREATE_NEW_PROCESS_GROUP
    )

def start_qv2ray_process(qv2ray_folder :str):
    return start_process('\"' + path.join(qv2ray_folder, qv2ray_bin_name) + '\"')

def kill_process(name):
    # TODO kill_process: impl
    pass

def relative_path(_path :str) -> str:
    # TODO relative_path: test on linux
    curdirve = path.splitdrive(path.realpath('.'))[0].upper()
    tardrive = path.splitdrive(_path)[0].upper()
    if curdirve == tardrive:
        return path.relpath(_path)
    else:
        return _path


if __name__ == '__main__':

    o = {
        "{port}": {
            'a': [
                {
                    "port": "{port}",
                    "node_group": "{node.group}",
                    "node_id": "{node.id}",
                }
            ]
        },
        "node_name": "{node.name}"
    }
    print(o)

    o = format_json_obj(o, {
        'port' : 3306,
        'node.id': 'ID\"123',
        'node.name': 'name\"123',
        'node.group': 'group\"123',
    })
    print(o)

    print(
        relative_path('C:/x/y/z')
    )
