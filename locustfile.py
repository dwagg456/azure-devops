from locust import HttpUser, TaskSet, task

input = {
    "CHAS":{"0":0},
    "RM":{"0":6.575},
    "TAX":{"0":296.0},
    "PTRATIO":{"0":15.3},
    "B":{"0":396.9},
    "LSTAT":{"0":4.98}
}

class MyTask(TaskSet):
    @task(1)
    def home_task(self):
        self.client.get("/")

    @task(2)
    def predict_task(self):
        self.client.post("/predict", json=input)

class MyLocust(HttpUser):
    tasks = [MyTask]

    min_wait = 1000
    max_wait = 3000

    host = "https://azure-devops-service.azurewebsites.net:443"
