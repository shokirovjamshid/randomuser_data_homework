import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    gender_list = []
    for i in data["results"]:
        if i["gender"]=="male":
            gender_list.append({"Male":1})
        else:
            gender_list.append({"Female":0})
    return gender_list
print(get_gender_users(get_data.get_data('randomuser_data.json')))
        
    