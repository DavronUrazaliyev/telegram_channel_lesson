from read_data import fromJson as data
import datetime

def get_post_per_month(data:dict,month:int)->int:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    dic = {i: 0 for i in range(1, 13)}

    for message in data.get("messages", []):
        if message.get("type") == "message" and "date_unixtime" in message:
            # Assuming "date_unixtime" field is present in the message
            m = datetime.datetime.fromtimestamp(int(message["date_unixtime"])).month
            dic[m] += 1

    return dic

data_dict = data("data/result.json")
posts_per_month = get_post_per_month(data_dict,0)
print(posts_per_month)