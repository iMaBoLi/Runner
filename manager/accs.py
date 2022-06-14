from .database import DB

def accs():
    return DB.get_key("USER_ACCS") or {}

def add_acc(user_id, number, session):
    all = accs()
    if not user_id in all:
        all.update({user_id: {}})
        DB.set_key("USER_ACCS", all)
    all = accs()[user_id]
    all.update({number: session})
    DB.set_key("USER_ACCS", all)
