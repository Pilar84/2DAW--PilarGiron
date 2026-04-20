from django.test import TestCase
from django.contrib.auth.models import User
from library.models import LibraryEntry

class LibraryEntryExternalIdLengthTests(TestCase):
    def test_health(self):
        # Precondiciones

        # Llamada (usando self.client y la ruta de la vista que queremos probar)
        response = self.client.get("/api/health/")

        # Comprobaciones
        # Comprobar el código HTTP que devuelve una vista
        self.assertEqual(response.status_code, 200)
        # Comprobar el contenido de la respuesta
        self.assertEqual(response.json(), {"status": "ok"})
        # Verifica que una clave existe dentro del JSON de la respuesta.
        self.assertIn("status", response.json())
        # Comprueba el valor concreto devuelto por la vista.
        self.assertEqual(response.json()["status"], "ok")
        # Asegura que la respuesta no contiene información que no debería aparecer.
        self.assertNotIn("paco", response.json())
        


class HealthViewInvalidMethodTests(TestCase):
    def test_health_endpoint_rejects_post_method(self):
        # Llamada usando un método incorrecto (POST)
        response = self.client.post("/api/health/")

        # Comprobación del código HTTP
        self.assertEqual(response.status_code, 405)
        
        
# -----------------------------
# EJERCICIO 4 — LISTADO DE ENTRADAS
#-----------------------------
class LibraryEntriesListTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="pilar", password="12345678")
        self.user2 = User.objects.create_user(username="juan", password="12345678")
        
        #entradas del user1
        LibraryEntry.objects.create(
            user=self.user1,
            external_game_id="game1",
            status="playing",
            hours_played=10
        )
        LibraryEntry.objects.create(
            user=self.user1,
            external_game_id="game2",
            status="completed",
            hours_played=20
        )
        
        #entrada del user2
        LibraryEntry.objects.create(
            user=self.user2,
            external_game_id="game3",
            status="playing",
            hours_played=5  
        )
        LibraryEntry.objects.create(
            user=self.user2,
            external_game_id="game4",
            status="dropped",
            hours_played=0      
        )
        
       
    def test_list_without_authentication(self):
        # Llamada sin login
        response = self.client.get("/api/library/entries/")

        # Comprobaciones
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "unauthorized")
        self.assertEqual(response.json()["message"], "No autenticado")

    def test_list_authenticated_user1(self):
        # Login user1
        self.client.post(
            "/api/auth/login/",
            data={"username": "pilar", "password": "12345678"},
            content_type="application/json"
        )

        # Llamada
        response = self.client.get("/api/library/entries/")

        # Comprobaciones
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

        external_ids = {entry["external_game_id"] for entry in data}
        self.assertEqual(external_ids, {"game1", "game2"})

    def test_list_two_users_isolated(self):
        # Login user2
        self.client.post(
            "/api/auth/login/",
            data={"username": "juan", "password": "12345678"},
            content_type="application/json"
        )

        # Llamada
        response = self.client.get("/api/library/entries/")

        # Comprobaciones
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # user2 tiene 2 entradas
        self.assertEqual(len(data), 2)

        external_ids = {entry["external_game_id"] for entry in data}
        self.assertEqual(external_ids, {"game3", "game4"})


# -----------------------------
# EJERCICIO 5 — DETALLE DE ENTRADAS
# -----------------------------
class LibraryEntryDetailTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="pilar", password="12345678")
        self.user2 = User.objects.create_user(username="juan", password="12345678")
        
        #Entradas del user1
        self.entry1 = LibraryEntry.objects.create(
            user=self.user1,
            external_game_id="game1",
            status="playing",
            hours_played=10 
        )
        
        #Entrada del user2
        self.entry2 = LibraryEntry.objects.create(
            user=self.user2,
            external_game_id="game2",
            status="completed",
            hours_played=20
        )   
        
    def test_detail_without_authentication(self):
        # Llamada sin login
        response = self.client.get(f"/api/library/entries/{self.entry1.id}/")

        # Comprobaciones        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "unauthorized")
        self.assertEqual(response.json()["message"], "No autenticado")        
        
    def test_detail_authenticated_user1(self): 
        # Login user1
        self.client.post("/api/auth/login/", data={"username": "pilar", "password": "12345678"}, content_type="application/json")
        
        # Llamada a la entrada de user1
        response = self.client.get(f"/api/library/entries/{self.entry1.id}/")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["external_game_id"], "game1")
        self.assertEqual(data["status"], "playing")
        self.assertEqual(data["hours_played"], 10)
        
    def test_detail_authenticated_other_user_entry(self):           
        # Login user1
        self.client.post("/api/auth/login/", data={"username": "pilar", "password": "12345678"}, content_type="application/json")
            
        # Llamada intentando acceder a entrada de user2
        response = self.client.get(f"/api/library/entries/{self.entry2.id}/")

        # Comprobaciones
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "not_found")
        self.assertEqual(response.json()["message"], "La entrada solicitada no existe")
        

# -----------------------------
# EJERCICIO 6— CADA ENTRADA ASOCIADA AL USUARIO REGISTRADO
# -----------------------------

class LibraryEntryCreateTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="pilar", password="12345678")
        self.user2 = User.objects.create_user(username="juan", password="12345678")
        
    def test_create_without_authentication(self):
        data = {
            "external_game_id": "game5",
            "status": "playing",
            "hours_played": 15
        }
        
        response = self.client.post("/api/library/entries/", data=data, content_type="application/json")    
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "unauthorized")
        self.assertEqual(response.json()["message"], "No autenticado")
        
        
    def test_create_authenticated_user1(self):
        self.client.post("/api/auth/login/", data={"username": "pilar", "password": "12345678"}, content_type="application/json")
        
        data = {
            "external_game_id": "game5",
            "status": "playing",
            "hours_played": 15
        }
        
        response = self.client.post("/api/library/entries/", data=data, content_type="application/json")    
        
        self.assertEqual(response.status_code, 201)

        #comprobar que la entrada pertenece al usuario autenticado
        entry = LibraryEntry.objects.get(external_game_id="game5")
        self.assertEqual(entry.user, self.user1)
        
        
    def test_create_isolated_users(self):
        # Login user1
        self.client.post("/api/auth/login/", data={"username": "pilar", "password": "12345678"}, content_type="application/json")
        
        # user1 crea una entrada
        self.client.post("/api/library/entries/", data={"external_game_id": "game5", "status": "playing", "hours_played": 15}, content_type="application/json")
        
        # Resetear sesión para evitar arrastrar login anterior
        self.client = self.client.__class__()

        # Login user2
        self.client.post("/api/auth/login/", data={"username": "juan", "password": "12345678"}, content_type="application/json")

        # User2 lista sus entradas
        response = self.client.get("/api/library/entries/")
        data = response.json()

        self.assertEqual(len(data), 0)