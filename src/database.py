from .pet_model import db


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()


def get_all(model):
    data = model.query.all()
    return data


def commit_changes():
    db.session.commit()
