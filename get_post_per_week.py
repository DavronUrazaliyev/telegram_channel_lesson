from read_data import fromJson
import datetime

def get_post_per_week(data: dict, target_month: int) -> dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        target_month (int): a number between 1 and 12

    Returns:
        dict: a dictionary with the number of posts for each week
    """
    dic = {} 
    for message in data.get("messages", []):
        if message.get("type") == "message" and "date_unixtime" in message:
            message_month = datetime.datetime.fromtimestamp(int(message["date_unixtime"])).month

            if message_month == target_month:
                week_number = datetime.datetime.fromtimestamp(int(message["date_unixtime"])).isocalendar()[1]
                dic[week_number] = dic.get(week_number, 0) + 1

    return dic

data_dict = fromJson("data/result.json")

target_month = 10
posts_per_week = get_post_per_week(data_dict, target_month)
print(posts_per_week)
