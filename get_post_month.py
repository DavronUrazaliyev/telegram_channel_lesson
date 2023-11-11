from read_data import fromJson as data
import datetime


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
def get_post_month(data:dict,month:int)->int:
    dic={}
    for i in range(1,13):
        dic[i]=0
    for i in data["messages"]:
        if i["type"]=="message":
            m=datetime.datetime.fromtimestamp(int(i["date_unixtime"])).month
            dic[m]+=1
    return dic
data=data("data/result.json")
a=get_post_month(data,2)
print(a)

    