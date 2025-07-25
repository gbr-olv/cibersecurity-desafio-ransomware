# cibersecurity-desafio-ransomware

Este é um projeto educacional criado para demonstrar, de forma simplificada, o funcionamento de um ransomware — um tipo de malware que criptografa arquivos da vítima e exige um pagamento para a descriptografia. **Este projeto tem fins exclusivamente didáticos**, voltado ao estudo de criptografia e segurança cibernética.

## ⚠️ Aviso Legal

> Este código é apenas para fins educacionais e de estudo. **Não há intenção de utilizar este projeto para atividades maliciosas ou ilegais.** O uso inadequado pode ter sérias consequências legais.

---

## 🔐 Como Funciona

### `encrypt.py`

Este script realiza a **criptografia** de um arquivo texto usando a biblioteca `pyaes` com AES no modo `CTR`.

**Etapas do script:**

1. Abre o arquivo original (`teste.txt`).
2. Lê os dados e remove o arquivo original.
3. Define uma chave de criptografia (`testeransomwares`).
4. Criptografa os dados com AES.
5. Salva o conteúdo criptografado em um novo arquivo com extensão `.ransomwaretroll`.

> Após a execução, o arquivo original é deletado e substituído por uma versão criptografada.

### `decrypt.py`

Este script faz a **descriptografia** do arquivo criptografado.

**Etapas do script:**

1. Abre o arquivo `.ransomwaretroll`.
2. Lê os dados criptografados.
3. Usa a mesma chave para reverter a criptografia.
4. Remove o arquivo criptografado.
5. Restaura o arquivo original (`teste.txt`).

---

## ⚠️ Disclaimer

Esse projeto é parte do Bootcamp de Cibersegurança da DIO. Forked from @cassiano-dio.
