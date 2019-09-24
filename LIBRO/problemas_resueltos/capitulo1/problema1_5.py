RADIO = float(input("Ingresa el radio del cilindro:"))
ALTU = float(input("Ingresa la altura del cilindro:"))
VOL = 3.141692 * (RADIO**2) * ALTU
ARE = 2 * 3.141592 * RADIO * ALTU
print(f"El volumen del cilindro es {VOL} cm y el área del cilindro es: {ARE} pulgadas")
