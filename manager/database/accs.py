from . import DB

def allacss(user_id):
    return DB.get_key("USER_ACCS")[user_id]

def add_acc(user_id, phone, session):
    all = allacss(user_id)    
    all["accs"].update({phone: session})
    DB.set_key("USER_ACCS", all)
    all = allacss(user_id)
    all["acc_count"] = len(all)
    DB.set_key("USER_ACCS", all)
