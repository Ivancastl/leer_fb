import os

# Ruta base donde está el script
base_path = os.path.dirname(os.path.abspath(__file__))

# Carpeta que contiene los archivos .txt
directory_path = os.path.join(base_path, "data")

def buscar_y_mostrar_coincidencias(file_path, keyword):
    """Busca la palabra clave en las líneas de un archivo y las muestra en la consola si hay coincidencias."""
    count = 0
    keyword_terms = keyword.lower().split()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            campos = line.strip().split(":")
            if all(any(term in campo.lower() for campo in campos) for term in keyword_terms):
                print(line.strip())  # Solo muestra la línea con coincidencia
                count += 1
    return count

def main():
    keyword = input("Introduce la palabra clave para buscar: ")
    total_coincidencias = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            coincidencias = buscar_y_mostrar_coincidencias(file_path, keyword)
            total_coincidencias += coincidencias

    print(f"\nTotal de coincidencias encontradas: {total_coincidencias}")

if __name__ == "__main__":
    main()

#https://lookup-id.com/    __user   en elements