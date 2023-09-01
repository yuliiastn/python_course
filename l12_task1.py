def isadmin(func):
    def wrapper(user_type, **kwargs):
        if user_type == 'admin':
            return func(user_type, **kwargs)
        return 'Permission denied'
    return wrapper


@isadmin
def show_cust_receipt(user_type=str):
    return "Here's your receipt"


print(show_cust_receipt('admin'))
