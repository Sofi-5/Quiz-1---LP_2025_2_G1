#Identificar las funcionalidades clave: retroceder, avanzar y cargar nuevas páginas.
#Considere usar una pila para realizar un seguimiento de las páginas visitadas.
#Defina los métodos que necesitará, como 'goBack()', 'goForward()' y 'loadPage(url)'.

class WebNavigator:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def load_page(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(f"Cargando: {url}")

    def go_back(self):
        if not self.back_stack:
            print("No hay páginas anteriores.")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Retrocediendo a: {self.current_page}")

    def go_forward(self):
        if not self.forward_stack:
            print("No hay páginas siguientes.")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Avanzando a: {self.current_page}")

    def current(self):
        return f"Página actual: {self.current_page}"


####################### simulación #########################################

# instancia del navegador
nav = WebNavigator()

# cargar páginas
nav.load_page("google.com")
nav.load_page("facebook.com")
nav.load_page("twitter.com")

# retroceder en el historial
nav.go_back()      
nav.go_back()      

# avanzar en el historial
nav.go_forward()   

# aargar una nueva página 
nav.load_page("youtube.com")

# avanzar 
nav.go_forward()

# current
print(nav.current())  

