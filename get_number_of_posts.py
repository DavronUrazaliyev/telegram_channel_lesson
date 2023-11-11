from read_data import fromJson as data
import datetime

def get_number_of_posts(data:dict,month:int)->int:
    return len(data.get("messages", []))
data=data("data/result.json")
a=get_number_of_posts(data,2)
print(a)