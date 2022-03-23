import time
from locust import HttpUser, task, between, User


class MinioEventsUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def minio_events(self):
        with self.client.post("/", json={"foo": 42, "bar": None}, catch_response=True) as response:
            try:
                if response.json()["greeting"] != "hello":
                    response.failure("Did not get expected value in greeting")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key 'greeting'")
