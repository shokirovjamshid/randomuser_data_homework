import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    count_users = 0
    for i in data["results"]:
        count_users+=1
    return count_users
print(get_count_users(get_data.get_data('randomuser_data.json')))
    
