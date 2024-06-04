from CCI import Historian
from service.db.cci_module import db
import json
import math

def get_value():
    tag_list = db.get_list('analogs')
    tags = []
    for tag in tag_list:
        value = str(db.get(tag))
        tags.append((tag, value))
    return tags

def get_history(tag):
    start_time = db.str2time('2024-03-24 00:00:00')
    end_time = db.now()
    times, values = db.get_history(tag, start_time, end_time)
    
    time = [db.time2str(time) for time in times]
    val = [float(value) if math.isfinite(float(value)) else None for value in values]
    return {"t": time, "v": val}

if __name__ == "__main__":
    tag_values = get_value()
    for tag, value in tag_values:
        print(f"Tag: {tag}, Value: {value}")
