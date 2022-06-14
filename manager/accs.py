from .database import DB

def accs():
    return DB.get_key("USER_ACCS") or {}

def add_acc(user_id, number, session):
    all = accs()[user_id]
    all.update({number: session})
    DB.set_key("USER_ACCS", all)
