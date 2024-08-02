def solution(id_pw, db):
    id_to_pw = {user_id : pw for user_id, pw in db}
    user_id, user_pw = id_pw
    if user_id not in id_to_pw:
        return "fail"
    if user_pw == id_to_pw[user_id]:
        return "login"
    else:
        return "wrong pw"