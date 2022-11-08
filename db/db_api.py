from db.create_db import session
from sqlalchemy import select, update
from db.models import Lan, Profile
import random


def user_language(id: int|str,language: str) -> None:
    sess = session()
    if select_lan(id):
        stmt = (update(Lan).where(Lan.user_id==id).values(user_language=language))
        sess.execute(stmt)
        sess.commit()
        sess.close()
        return
    else:
        sess.add(Lan(id,language))
        sess.commit()
        sess.close()

def select_lan(id: int|str) -> str|None:
    sess = session()
    stmt = select(Lan).where(Lan.user_id == id)
    language = None
    for row in sess.execute(stmt):
        language = row[0].user_language
    sess.close()
    return language

def check_profile(id: int|str) -> list[str]|None:
    sess = session()
    stmt = select(Profile).where(Profile.user_id == id)
    prof = None
    for row in sess.execute(stmt):
        str_db = row[0]
        prof = [str_db.user_id,str_db.age,str_db.gender,str_db.like,str_db.city,str_db.name,str_db.description,str_db.photo]
    sess.close()
    return prof

def user_profile(id: str,age: str,gender: str,like: str,city: str,name: str,description: str,photo: str) -> None:
    sess = session()
    if check_profile(id):
        stmt = (update(Profile).where(Profile.user_id==id).values(age=age,gender=gender,like=like,city=city,name=name,description=description,photo=photo))
        sess.execute(stmt)
        sess.commit()
        sess.close()
        return
    else:
        sess.add(Profile(id,age,gender,like,city,name,description,photo))
        sess.commit()
        sess.close()

def ankets(gender: str,age: str,like: str,id: str,city: str) -> list[str]:
    sess = session()
    stmt = select(Profile).where(Profile.user_id != id, Profile.age==age,Profile.gender == gender, Profile.like == like, Profile.city == city)
    prof = []
    for row in sess.execute(stmt):
        str_db = row[0]
        prof.append([str_db.user_id,str_db.age,str_db.gender,str_db.like,str_db.city,str_db.name,str_db.description,str_db.photo])
    sess.close()
    if len(prof)==1:
        return prof[0]
    if len(prof)>1:
        return random.choice(prof)

def select_all_users() -> Sequence[Row[Tuple[int]]]:
    sess = session()
    stmt = select(Profile.user_id)
    return sess.execute(stmt).fetchall()

