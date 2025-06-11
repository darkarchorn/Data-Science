from app.models.human import HumanImpl
from app.models.database import DatabaseConnection

db = DatabaseConnection("humans.db")
conn = db.getConnection()

def add_human(data):
    human = HumanImpl(data["id"], data["name"], data["age"], data["job"])
    conn.execute("INSERT INTO Human (id, name, age, job) VALUES (?, ?, ?, ?)",
                 (human.getProperty("id"), human.getProperty("name"),
                  human.getProperty("age"), human.getProperty("job")))
    conn.commit()
    return "Human added successfully"

def get_human(human_id):
    cursor = conn.execute("SELECT * FROM Human WHERE id = ?", (human_id,))
    return cursor.fetchone()

def list_humans():
    cursor = conn.execute("SELECT * FROM Human")
    return cursor.fetchall()
