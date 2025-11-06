def consulta_datos(input_text):
    base_datos_fake = {
        "ventas": "Ventas totales del trimestre: $120.000.000 CLP.",
        "productividad": "El equipo logró un 15% más productividad respecto al mes anterior.",
        "clientes": "Se sumaron 50 nuevos clientes durante el periodo.",
        "asistencia": "El 90% del personal cumplió con la jornada completa sin ausencias."
    }
    for clave, valor in base_datos_fake.items():
        if clave in input_text.lower():
            return valor
    return "No se encontraron datos relevantes para la búsqueda solicitada."
