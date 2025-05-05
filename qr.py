import qrcode

# URL del repositorio de GitHub
url = "https://acruxzx.github.io/aviso-carnet/"

# Crear objeto QR
qr = qrcode.QRCode(
    version=1,  # tamaño del QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # nivel de corrección
    box_size=10,  # tamaño de cada cuadro
    border=4  # grosor del borde
)

qr.add_data(url)
qr.make(fit=True)

# Crear imagen
img = qr.make_image(fill="black", back_color="white")

# Guardar imagen
img.save("repositorio_qr.png")

print("✅ Código QR generado como 'repositorio_qr.png'")
