
import qrcode

# Dados que você deseja codificar no QR code
dados = "Andre Andrino - 061-982423430 andreandrino@hotmail.com"

# Criação do objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Versão do QR code (controle de tamanho)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
    box_size=10,  # Tamanho de cada quadrado no QR code
    border=4,  # Tamanho da borda (em quadrados)
)

# Adicionando dados ao QR code
qr.add_data(dados)
qr.make(fit=True)

# Criação da imagem do QR code
imagem_qr = qr.make_image(fill_color="black", back_color="white")

# Salvando a imagem do QR code
imagem_qr.save("andre.png")

print("QR code gerado e salvo como 'qrcode_exemplo.png'.")
