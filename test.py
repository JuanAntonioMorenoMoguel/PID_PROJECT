import os
from cnn import analisis_ia

def test_images_in_validation_folder():
    validation_folder = "images/validation"  # Cambia esto si la carpeta tiene otra ruta
    results = {"Bien": 0, "Mal":0}  # Inicializa el contador de resultados

    if not os.path.exists(validation_folder):
        print(f"La carpeta '{validation_folder}' no existe.")
        return

    for file_name in os.listdir(validation_folder):
        file_path = os.path.join(validation_folder, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                result, color = analisis_ia(file_path)
                if(file_name.__contains__("malign")):
                    if result == "maligno":
                        results["Bien"] = results["Bien"] + 1  
                    else:
                        results["Mal"] = results["Mal"] + 1
                    print(results)
                elif(file_name.__contains__("benign")):
                    if result == "benigno":
                        results["Bien"] = results["Bien"] + 1
                    else:
                        results["Mal"] = results["Mal"] + 1
                    print(results)
                else:
                    print(f"El nombre del archivo '{file_name}' no contiene 'malign' o 'benign'.")
            except Exception as e:
                print(f"Error al analizar la imagen {file_name}: {e}")

    # Guardar los resultados en un archivo de texto
    with open("validation_results.txt", "w") as result_file:
        for file_name, result, color in results:
            result_file.write(f"{file_name}: {result}, {color}\n")

    print("Pruebas completadas. Resultados guardados en 'validation_results.txt'.")

if __name__ == "__main__":
    test_images_in_validation_folder()