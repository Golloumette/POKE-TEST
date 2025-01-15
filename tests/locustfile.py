from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    
    @task(1)
    def battle_pokemons(self):
        self.client.post("/pokemons/battle/", json={
            "first_pokemon_id": 1,
            "second_pokemon_id": 2
        })

    @task(2)
    def get_random_pokemons(self):
        self.client.get("/pokemons/pokemonsRandom/")
        

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  
    host = "http://127.0.0.1:8000"  