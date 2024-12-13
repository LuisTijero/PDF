import pandas as pd

# Ruta del archivo CSV ordenado
libro_edit = 'libro_word.docx'

try:
    # Leer el archivo CSV ordenado
    libro_edita = pd.read_pdf(libro_edit)
    
    # Exportar a Excel
    archivo_word = 'data_analisis.docx'
    libro_edita.to_excel(archivo_word, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_word}")
except Exception as e:
    print(f"Error al exportar los datos: {e}")
    
    
