# 12. Crie um programa que traduza qualquer texto em qualquer idioma para o português.

from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')#source='auto' identifica em qual idioma esta / target='pt' pra qual é pra traduzir

while True:
    texto = input('Digite seu texto: ')
    texto_traduzido = tradutor.translate(texto) 
    print(texto_traduzido)

    repetir = input('Deseja traduzir outro texto (s/n)? ').lower()
    if repetir == 's':
        continue
    else:
        break