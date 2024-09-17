
# 13. Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.
# importa bibliotecas
import pyautogui as auto
import time

# Define o tempo de pausa padrão entre os comandos do pyautogui
auto.PAUSE = 2

# Abre o navegador (Edge)
auto.press('win')
auto.write('edge')
auto.press('enter')

# Espera um tempo para o navegador abrir completamente
time.sleep(5)

# Digita o endereço do YouTube e pressiona Enter
auto.write('www.youtube.com')
auto.press('enter')

# Espera a página carregar
time.sleep(5)

# Se a barra de pesquisa não estiver ativa, use tab para selecioná-la (pode variar conforme a interface)
# Este trecho simula a navegação até o campo de pesquisa
auto.press('tab', presses=4)  # Ajuste o número de 'tabs' conforme necessário

# Digita a pesquisa desejada e pressiona Enter
auto.write('videoaulas sobre Pandas')
auto.press('enter')

# Espera os resultados carregarem
time.sleep(5)
