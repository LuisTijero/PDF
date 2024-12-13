import pandas as pd

# Ruta del archivo CSV intermedio
archivo_word = 'libro.pdf'

try:
    # Leer el archivo CSV
    data = pd.read_pdf(libro.pdf)
    
    # Ordenar los datos por nombre
    data_ordenada = data.sort_values(by='Nombre1')
    
    # Exportar a Excel
    archivo_excel = 'clientes_ordenados.xlsx'
    data_ordenada.to_excel(libro.pdf, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")