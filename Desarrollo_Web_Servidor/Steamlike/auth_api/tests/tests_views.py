from django.test import TestCase
from django.contrib.auth.models import User


#test para validar los registros de usuarios-ejercicio 1
class AuthRegisterTests(TestCase):
    def test_register_user(self):
        # Precondiciones
        datos ={
            "username": "pilar",
            "password": "12345678",
        }
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)
        self.assertIn("username", data)
        self.assertNotIn("password", data)
        self.assertTrue(User.objects.filter(username="pilar").exists())
        
        
    def test_register_empty_json(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos)
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        
        
    def test_register_missing_username(self): 
        # Precondiciones
        datos ={"username": "pilar"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json") 
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        
    def test_register_short_password(self):
        # Precondiciones
        datos ={"username": "pilar", "password": "123"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        
    def test_register_duplicate_username(self):
        # Precondiciones
        User.objects.create_user(username="pilar", password="12345678")
        datos ={"username": "pilar", "password": "12345678"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        

      
        #ejercicio 2: test para validar login de usuarios
class AuthLoginTests(TestCase):
    def setUp(self):
        #Precondiciones
        User.objects.create_user(username="pilar", password="12345678")
        
    def test_login_user(self):
        # Precondiciones
        datos ={"username": "pilar", "password": "12345678"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("id", data)
        self.assertIn("username", data)
        self.assertNotIn("password", data)  
        
    def test_login_wrong_password(self):
        # Precondiciones
        datos ={"username": "pilar", "password": "wrongpassword"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "Credenciales incorrectas")
        
    def test_login_missing_username(self):
        # Precondiciones
        datos = {"username": "pilar"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")  
        
    def test_login_missing_password(self):
        # Precondiciones
        datos = {"password": "12345678"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        
    def test_login_missing_username_and_password(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
    
    def test_login_empty_json(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")  
        
    
    #Ejercicio 3: test para validar la vista me, que devuelve los datos del usuario logueado
    
class AuthMeTests(TestCase): 
    
    def setUp(self):
        self.user = User.objects.create_user(username="pilar", password="12345678")
        
        
    def test_me_without_authentication(self):
        # Precondiciones
        # (no hacemos login)

        # Llamada
        response = self.client.get("/api/users/me/")

        # Comprobaciones
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "unauthorized")
        self.assertEqual(response.json()["message"], "No autenticado")


    def test_me_after_login(self):
        # Precondiciones
        login_data = {"username": "pilar", "password": "12345678"}
        self.client.post("/api/auth/login/", data=login_data, content_type="application/json")

        # Llamada
        response = self.client.get("/api/users/me/")

        # Comprobaciones
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], self.user.id)
        self.assertEqual(data["username"], self.user.username)