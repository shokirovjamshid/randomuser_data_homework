import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    email_list = []
    for i in data["results"]:
        email_list.append(i["email"])
    return email_list
print(get_email(get_data.get_data('randomuser_data.json')))