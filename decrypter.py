import os
import pyaes

## abrir o arquivo criptografado

file_name = 'teste.txt.ransomwaretroll' # Nome do arquivo criptografado
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

## remover o arquivo descriptografado
os.remove(file_name)

## criar um novo arquivo descriptografado

new_file = 'teste.txt' # Nome do arquivo descriptografado
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()
print('Arquivo descriptografado com sucesso!')
