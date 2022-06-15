from . import DB

def allacss():
    return DB.get_key("USER_ACCS")

def add_acc(user_id, phone, session):
    all = allacss()    
    all[user_id]["accs"].update({phone: session})
    DB.set_key("USER_ACCS", all)
    all = allacss()
    all[user_id]["acc_count"] = len(all)
    DB.set_key("USER_ACCS", all)
