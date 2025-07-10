import json
from datetime import datetime
def convert_time_to_ms(iso_time):
   time_object = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
    return int(time_object.timestamp() * 1000)
def fix_data1(data_list):
    fixed_list = []

    for item in data_list:
        new_item = {
            "timestamp": convert_time_to_ms(item["timestamp"]),
            "machine_id": item["machine_id"],
            "metrics": {
                "temperature": item["metrics"]["temperature"],
                "vibration": item["metrics"]["vibration"],
                "pressure": item["metrics"]["pressure"]
            }
        }
        fixed_list.append(new_item)

    return fixed_list
def fix_data2(data_list):
    fixed_list = []

    for item in data_list:
        new_item = {
            "timestamp": item["timestamp"], 
            "machine_id": item["id"],
            "metrics": {
                "temperature": item["temperature"],
                "vibration": item["vibration_level"],
                "pressure": item["pressure"]
            }
        }
        fixed_list.append(new_item)

    return fixed_list
def unify_data(data1, data2):
    part1 = fix_data1(data1)
    part2 = fix_data2(data2)
    return part1 + part2
