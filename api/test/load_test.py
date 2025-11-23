from locust import HttpUser, between, task
from time import time

# locust server port 8089
class WebsiteUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 1)

    def on_start(self):
        self.counter = 0
    
    @task
    def create_task(self):
        user_id = id(self)
        unique_title = f"Task Title {user_id}-{self.counter}-{int(time() * 1000)}"
        
        self.client.post('/', json={
            "title": unique_title,
            "description": "This is a recurring load test task.",
            "priority": "Low",
            "status": "incomplete"})
        self.counter += 1

    @task
    def retrieve_tasks(self):
        self.client.get("/")