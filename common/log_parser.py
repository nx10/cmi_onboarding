from abc import ABC
import pandas as pd
import json


class CpacLogField(ABC):
    """Small utility for cpac log file definitions"""

    ID = 'id'
    HASH = 'hash'
    DATE_TIME_START = 'start'
    DATE_TIME_END = 'finish'
    RUNTIME_THREADS = 'runtime_threads'
    RUNTIME_MEMORY_GB = 'runtime_memory_gb'
    ESTIMATED_MEMORY_GB = 'estimated_memory_gb'
    NUM_THREADS = 'num_threads'

    @classmethod
    def date_time_fields(cls):
        return cls.DATE_TIME_START, cls.DATE_TIME_END


# Loosely based on cpac.helpers.cpac_parse_resources.load_runtime_stats
def cpac_log_as_data_table(callback):
    with open(callback, 'r') as file:
        logs = [json.loads(log) for log in file.readlines()]

    records = [
        dict(log) for log in logs if CpacLogField.DATE_TIME_START in log.keys()
    ]

    df = pd.DataFrame.from_records(records)

    for date_field in CpacLogField.date_time_fields():
        df[date_field] = pd.to_datetime(df[date_field])

    return df
