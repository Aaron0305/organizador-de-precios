import csv

# Precios actualizados
updated_prices = {
    'Celery': 1.19,
    'Garlic': 3.07,
    'Lemon': 1.27
}

# Nombre de los archivos de entrada y salida
input_file = r'C:\Users\DELL\Documents\Visual\produceSales.csv'
output_file = r'C:\Users\DELL\Documents\Visual\produceSales_updated.csv'

# Abrir archivo de entrada en modo lectura
with open(input_file, mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    headers = reader.fieldnames  # Obtener los encabezados
    
    # Verificar si todos los encabezados necesarios están presentes
    required_headers = ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD']
    for header in required_headers:
        if header not in headers:
            print(f'Error: No se encontró el encabezado "{header}" en el archivo CSV.')
            exit(1)

    # Agregar 'TOTAL REVENUE' a la lista de encabezados
    headers.append('TOTAL REVENUE')

    # Crear lista para almacenar las filas actualizadas
    updated_rows = []
    
    # Procesar cada fila
    for row in reader:
        produce = row['PRODUCE']
        cost_per_pound = float(row['COST PER POUND'])
        pounds_sold = float(row['POUNDS SOLD'])
        
        # Actualizar precio y recalcular ingresos totales si es necesario
        if produce in updated_prices:
            # Actualizar precio por libra
            row['COST PER POUND'] = str(updated_prices[produce])
            # Recalcular ingresos totales
            new_total_revenue = pounds_sold * updated_prices[produce]
            row['TOTAL REVENUE'] = '{:.2f}'.format(new_total_revenue)  # Formatear a dos decimales
        
        # Agregar fila actualizada a la lista
        updated_rows.append(row)

# Escribir el archivo modificado
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()  # Escribir encabezados actualizados
    writer.writerows(updated_rows)  # Escribir filas actualizadas

print(f'Archivo "{output_file}" ha sido actualizado con éxito.')