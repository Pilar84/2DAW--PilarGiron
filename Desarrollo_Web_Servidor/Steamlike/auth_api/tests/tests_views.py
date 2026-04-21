from django.test import TestCase
from django.contrib.auth.models import User



# ============================================================
# EJERCICIO 1 — TESTS DE REGISTRO
# ============================================================  
#test que comprueba un registro válido
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
        
    #Test que comprueba que enviar un JSON vacío provoca error 400   
    def test_register_empty_json(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos)
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        
    # Test que comprueba que falta el campo password → error 400 validation_error    
    def test_register_missing_username(self): 
        # Precondiciones
        datos ={"username": "pilar"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json") 
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
    
     # Test que comprueba que la contraseña es demasiado corta 
    def test_register_short_password(self):
        # Precondiciones
        datos ={"username": "pilar", "password": "123"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
    
    # Test que comprueba que el username ya existe
    def test_register_duplicate_username(self):
        # Precondiciones
        User.objects.create_user(username="pilar", password="12345678")
        datos ={"username": "pilar", "password": "12345678"}
        
        # Llamada
        response = self.client.post("/api/auth/register/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
        

      
# ============================================================
# EJERCICIO 2 — TESTS DE login
# ============================================================  

#Test que comprueba un login valido
#Crea un usuario válido para los tests de login
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
    
    # Test de contraseña incorrecta 
    def test_login_wrong_password(self):
        # Precondiciones
        datos ={"username": "pilar", "password": "wrongpassword"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "Credenciales incorrectas")
    
    # Test que comprueba que falta username → error 400  
    def test_login_missing_username(self):
        # Precondiciones
        datos = {"username": "pilar"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")  
    
    # Test que comprueba que falta password → error 400 
    def test_login_missing_password(self):
        # Precondiciones
        datos = {"password": "12345678"}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
    
    # Test que comprueba que faltan ambos campos → error 400    
    def test_login_missing_username_and_password(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")
    
    # Test que comprueba que un JSON vacío
    def test_login_empty_json(self):
        # Precondiciones
        datos = {}
        
        # Llamada
        response = self.client.post("/api/auth/login/", data=datos, content_type="application/json")
        
        # Comprobaciones
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "validation_error")  
        
#----------------------------------------------------  
#Ejercicio 3: test para validar la vista me, que devuelve los datos del usuario logueado
#----------------------------------------------------  


class AuthMeTests(TestCase): 
    
    #crea un usuario para los tests
    def setUp(self):
        self.user = User.objects.create_user(username="pilar", password="12345678")
        
    #test sin autenticar  
    def test_me_without_authentication(self):
        # Precondiciones
        # (no hacemos login)

        # Llamada
        response = self.client.get("/api/users/me/")

        # Comprobaciones
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "unauthorized")
        self.assertEqual(response.json()["message"], "No autenticado")


    #test con autenticacion
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