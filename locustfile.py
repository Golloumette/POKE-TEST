from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def get_pokemons(self):
        self.client.get("/pokemons/?skip=0&limit=100")

    @task(2)
    def get_items(self):
        self.client.get("/items/?skip=0&limit=100")

    @task(3)
    def battle_pokemons(self):
        self.client.post("/pokemons/battle/", json={
            "first_pokemon_id": 1,
            "second_pokemon_id": 2
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Temps d'attente entre les tâches (en secondes)