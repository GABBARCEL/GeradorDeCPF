# Gerador de CPF Matemático

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Um gerador de **CPFs válidos matematicamente**, feito em Python. Este projeto **gera números aleatórios e calcula os dígitos verificadores corretamente**, sem depender de CPFs reais. Ideal para testes, simulações e aprendizado.

---

## Funcionalidades

- Gera **9 dígitos aleatórios** para formar a base do CPF.  
- Calcula **DV1 e DV2** corretamente usando os pesos do algoritmo oficial do CPF.  
- Retorna o **CPF completo de 11 dígitos**, pronto para uso em testes ou validações.  
- Possibilidade de **retornar o CPF formatado** como `XXX.XXX.XXX-XX`.  
- Código **limpo, modular e reutilizável**.

---

## Como funciona

1. **Geração da base do CPF**: 9 números aleatórios (0–9).  
2. **Cálculo do primeiro dígito verificador (DV1)**:  
   - Multiplica cada dígito pelo peso correspondente (10 → 2)  
   - Soma os produtos  
   - Aplica `(soma * 10) % 11`  
   - Se o resultado for 10, DV1 = 0  
3. **Cálculo do segundo dígito verificador (DV2)**:  
   - Usa os 9 dígitos originais + DV1  
   - Multiplica cada dígito pelo peso correspondente (11 → 2)  
   - Soma os produtos  
   - Aplica `(soma * 10) % 11`  
   - Se o resultado for 10, DV2 = 0  
4. Retorna o CPF completo: 9 dígitos + DV1 + DV2

---

## Exemplo de uso

```python
from main import GenCpf

# Gerando uma base aleatória
randomCPF = [5, 3, 8, 1, 2, 9, 0, 4, 7]

# Calculando os dígitos verificadores
cpf_completo = GenCpf(randomCPF)

# CPF completo como lista de dígitos
print("CPF gerado:", cpf_completo)
# Saída: [5, 3, 8, 1, 2, 9, 0, 4, 7, DV1, DV2]

# CPF formatado tradicionalmente
cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*cpf_completo)
print("CPF formatado:", cpf_formatado)
# Saída: 538.129.047-XY
# Gerador de CPF Matemático

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Um gerador de **CPFs válidos matematicamente**, feito em Python. Este projeto **gera números aleatórios e calcula os dígitos verificadores corretamente**, sem depender de CPFs reais. Ideal para testes, simulações e aprendizado.

---

## Funcionalidades

- Gera **9 dígitos aleatórios** para formar a base do CPF.  
- Calcula **DV1 e DV2** corretamente usando os pesos do algoritmo oficial do CPF.  
- Retorna o **CPF completo de 11 dígitos**, pronto para uso em testes ou validações.  
- Possibilidade de **retornar o CPF formatado** como `XXX.XXX.XXX-XX`.  
- Código **limpo, modular e reutilizável**.

---

## Como funciona

1. **Geração da base do CPF**: 9 números aleatórios (0–9).  
2. **Cálculo do primeiro dígito verificador (DV1)**:  
   - Multiplica cada dígito pelo peso correspondente (10 → 2)  
   - Soma os produtos  
   - Aplica `(soma * 10) % 11`  
   - Se o resultado for 10, DV1 = 0  
3. **Cálculo do segundo dígito verificador (DV2)**:  
   - Usa os 9 dígitos originais + DV1  
   - Multiplica cada dígito pelo peso correspondente (11 → 2)  
   - Soma os produtos  
   - Aplica `(soma * 10) % 11`  
   - Se o resultado for 10, DV2 = 0  
4. Retorna o CPF completo: 9 dígitos + DV1 + DV2

---

## Exemplo de uso

```python
from cpf_generator import GenCpf

# Gerando uma base aleatória
randomCPF = [5, 3, 8, 1, 2, 9, 0, 4, 7]

# Calculando os dígitos verificadores
cpf_completo = GenCpf(randomCPF)

# CPF completo como lista de dígitos
print("CPF gerado:", cpf_completo)
# Saída: [5, 3, 8, 1, 2, 9, 0, 4, 7, DV1, DV2]

# CPF formatado tradicionalmente
cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*cpf_completo)
print("CPF formatado:", cpf_formatado)
# Saída: 538.129.047-XY