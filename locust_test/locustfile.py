from locust import HttpUser, task, between

class MLUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def upload_image(self):
        with open("test.jpg", "rb") as img:
            self.client.post(
                "/classify",
                files={"image": ("test.jpg", img, "image/jpeg")}
            )