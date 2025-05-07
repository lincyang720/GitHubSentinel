from src.database import SessionLocal, Subscription

def add_subscription(repo_full_name):
    db = SessionLocal()
    sub = Subscription(repo=repo_full_name)
    db.add(sub)
    db.commit()

def list_subscriptions():
    db = SessionLocal()
    return db.query(Subscription).all()
