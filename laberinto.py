import os

class LaberintoSolver:
    def __init__(self):
        self.filas = 0
        self.columnas = 0
        self.laberinto = []
        self.entrada = None
        self.salida = None
        self.visitado = set()
        self.direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
    
    def cargar_laberinto(self, archivo):
        """Carga el laberinto desde un archivo de texto"""
        try:
            with open(archivo, 'r') as f:
                lineas = f.readlines()
            
            # Limpiar líneas y eliminar vacías
            lineas = [linea.strip() for linea in lineas if linea.strip()]
            
            if len(lineas) < 3:
                print("Error: Archivo incompleto")
                return False
            
            # Leer dimensiones
            self.filas = int(lineas[0])
            self.columnas = int(lineas[1])
            
            # Leer laberinto
            self.laberinto = []
            for i in range(2, 2 + self.filas):
                if i < len(lineas):
                    fila = list(lineas[i].replace(' ', ''))  # Eliminar espacios
                    # Asegurar que todas las filas tengan la misma longitud
                    while len(fila) < self.columnas:
                        fila.append('1')  # Rellenar con paredes si es necesario
                    self.laberinto.append(fila[:self.columnas])
            
            # Encontrar entrada y salida
            self.entrada = None
            self.salida = None
            
            for i in range(self.filas):
                for j in range(self.columnas):
                    if self.laberinto[i][j] == 'E':
                        self.entrada = (i, j)
                    elif self.laberinto[i][j] == 'S':
                        self.salida = (i, j)
            
            if not self.entrada:
                print("Error: No se encontró la entrada (E)")
                return False
            
            if not self.salida:
                print("Error: No se encontró la salida (S)")
                return False
            
            return True
            
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo '{archivo}'")
            return False
        except Exception as e:
            print(f"Error al cargar el laberinto: {e}")
            return False
    
    def es_valido(self, fila, columna):
        """Verifica si una posición es válida para moverse"""
        return (0 <= fila < self.filas and 
                0 <= columna < self.columnas and 
                self.laberinto[fila][columna] != '1' and 
                (fila, columna) not in self.visitado)
    
    def resolver(self):
        """Resuelve el laberinto usando backtracking con pila"""
        if not self.entrada or not self.salida:
            return None
        
        pila = []
        self.visitado = set()
        
        # Comenzar desde la entrada
        pila.append(self.entrada)
        self.visitado.add(self.entrada)
        
        # Mapa para reconstruir el camino
        padre = {self.entrada: None}
        
        while pila:
            actual = pila[-1]  # Mirar el tope de la pila
            
            if actual == self.salida:
                # Reconstruir camino desde salida hasta entrada
                camino = []
                paso = actual
                while paso:
                    camino.append(paso)
                    paso = padre[paso]
                return camino[::-1]  # Invertir para que vaya de entrada a salida
            
            # Buscar siguiente movimiento válido
            movio = False
            for df, dc in self.direcciones:
                nueva_fila = actual[0] + df
                nueva_col = actual[1] + dc
                nueva_pos = (nueva_fila, nueva_col)
                
                if self.es_valido(nueva_fila, nueva_col):
                    pila.append(nueva_pos)
                    self.visitado.add(nueva_pos)
                    padre[nueva_pos] = actual
                    movio = True
                    break
            
            # Si no se pudo mover, hacer backtracking
            if not movio:
                pila.pop()
        
        return None  # No se encontró solución
    
    def imprimir_laberinto(self, camino=None):
        """Imprime el laberinto, opcionalmente marcando el camino solución"""
        if camino is None:
            camino = []
        
        print(f"\nLaberinto {self.filas}x{self.columnas}:")
        for i in range(self.filas):
            for j in range(self.columnas):
                pos = (i, j)
                if pos == self.entrada:
                    print('E', end=' ')
                elif pos == self.salida:
                    print('S', end=' ')
                elif pos in camino:
                    print('*', end=' ')  # Marcar camino solución
                else:
                    print(self.laberinto[i][j], end=' ')
            print()
    
    def imprimir_ruta(self, camino):
        """Imprime la ruta de solución"""
        if not camino:
            print("No se encontró solución para el laberinto.")
            return
        
        print("\nRuta de solución encontrada:")
        for i, paso in enumerate(camino):
            if i == 0:
                print(f"Paso {i}: Entrada -> {paso}")
            elif i == len(camino) - 1:
                print(f"Paso {i}: {paso} -> Salida")
            else:
                print(f"Paso {i}: {paso}")
        
        print(f"\nLongitud del camino: {len(camino)} pasos")
        print(f"Coordenadas completas: {camino}")

def crear_laberinto_propuesto():
    """Crea el laberinto propuesto en la imagen"""
    contenido = """8
10
1111111111
1E00100001
1011101011
1000001001
1010111001
1001000001
1101011111
1001S00001"""
    
    with open('laberinto_propuesto.txt', 'w') as f:
        f.write(contenido)
    print("✓ Laberinto propuesto creado como 'laberinto_propuesto.txt'")

def crear_nuevo_laberinto():
    """Permite al usuario crear un nuevo laberinto"""
    print("\n--- CREAR NUEVO LABERINTO ---")
    
    nombre = input("Nombre del archivo (sin extensión .txt): ").strip()
    if not nombre:
        nombre = "nuevo_laberinto"
    
    archivo = f"{nombre}.txt"
    
    try:
        # Dimensiones
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))
        
        print(f"\nCreando laberinto {filas}x{columnas}")
        print("Instrucciones:")
        print("• Use '1' para paredes")
        print("• Use '0' para pasillos") 
        print("• Use 'E' para la entrada")
        print("• Use 'S' para la salida")
        print("• Escriba cada fila en una línea sin espacios")
        print()
        
        laberinto = []
        print("Ingrese las filas del laberinto:")
        
        for i in range(filas):
            while True:
                fila = input(f"Fila {i+1}: ").strip()
                if len(fila) != columnas:
                    print(f"Error: La fila debe tener exactamente {columnas} caracteres")
                    continue
                
                # Validar caracteres
                valido = True
                for char in fila:
                    if char not in ['1', '0', 'E', 'S']:
                        print("Error: Caracteres válidos son: 1, 0, E, S")
                        valido = False
                        break
                
                if valido:
                    laberinto.append(fila)
                    break
        
        # Verificar que hay exactamente una E y una S
        entrada_count = sum(fila.count('E') for fila in laberinto)
        salida_count = sum(fila.count('S') for fila in laberinto)
        
        if entrada_count != 1:
            print("Error: Debe haber exactamente una entrada (E)")
            return
        if salida_count != 1:
            print("Error: Debe haber exactamente una salida (S)")
            return
        
        # Guardar archivo
        with open(archivo, 'w') as f:
            f.write(f"{filas}\n")
            f.write(f"{columnas}\n")
            for fila in laberinto:
                f.write(f"{fila}\n")
        
        print(f"✓ Laberinto guardado como '{archivo}'")
        
    except ValueError:
        print("Error: Las dimensiones deben ser números enteros")
    except Exception as e:
        print(f"Error al crear el laberinto: {e}")

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("          RESOLVEDOR DE LABERINTOS")
    print("="*50)
    print("1. Resolver laberinto propuesto")
    print("2. Resolver laberinto desde archivo")
    print("3. Crear nuevo laberinto")
    print("4. Salir")
    print("="*50)

def main():
    solver = LaberintoSolver()
    
    # Crear laberinto propuesto si no existe
    if not os.path.exists('laberinto_propuesto.txt'):
        crear_laberinto_propuesto()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            # Resolver laberinto propuesto
            print("\n--- LABERINTO PROPUESTO ---")
            if solver.cargar_laberinto('laberinto_propuesto.txt'):
                solver.imprimir_laberinto()
                print("\nResolviendo laberinto...")
                camino = solver.resolver()
                
                if camino:
                    print("¡Solución encontrada!")
                    solver.imprimir_laberinto(camino)
                    solver.imprimir_ruta(camino)
                else:
                    print("No se pudo encontrar una solución para el laberinto.")
                    solver.imprimir_laberinto()
        
        elif opcion == '2':
            # Resolver laberinto desde archivo
            print("\n--- RESOLVER LABERINTO DESDE ARCHIVO ---")
            archivo = input("Ingrese el nombre del archivo (ej: laberinto.txt): ").strip()
            
            if not archivo.endswith('.txt'):
                archivo += '.txt'
            
            if not os.path.exists(archivo):
                print(f"Error: El archivo '{archivo}' no existe")
                continue
            
            if solver.cargar_laberinto(archivo):
                solver.imprimir_laberinto()
                print("\nResolviendo laberinto...")
                camino = solver.resolver()
                
                if camino:
                    print("¡Solución encontrada!")
                    solver.imprimir_laberinto(camino)
                    solver.imprimir_ruta(camino)
                else:
                    print("No se pudo encontrar una solución para el laberinto.")
                    solver.imprimir_laberinto()
        
        elif opcion == '3':
            # Crear nuevo laberinto
            crear_nuevo_laberinto()
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor seleccione 1-4.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()