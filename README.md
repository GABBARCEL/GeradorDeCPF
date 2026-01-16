# Gerador de CPF Matemático

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Um gerador de **CPFs válidos matematicamente**, feito em Python. Este projeto gera números aleatórios e calcula os dígitos verificadores corretamente, sem depender de CPFs reais. Ideal para testes, simulações e aprendizado.

---

## Funcionalidades

- Gera **9 dígitos aleatórios** para formar a base do CPF.  
- Calcula **DV1 e DV2** corretamente usando os pesos do algoritmo oficial do CPF.  
- Retorna o **CPF completo de 11 dígitos**, pronto para uso em testes ou validações.  
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

## Observações

- Os CPFs gerados **não são reais**, apenas **válidos matematicamente**.  
- Pode ser usado em testes, validação de sistemas, simulações ou aprendizado sobre o algoritmo do CPF.  
- O código é **modular**, permitindo reutilizar a função de cálculo de produtos para outros tipos de validação.

---

## Tecnologias

- Python 3.x  
- Biblioteca `secrets` para gerar números aleatórios seguros

---

## Contribuição

Contribuições são bem-vindas! Você pode:

- Melhorar a geração de números aleatórios  
- Criar versões que retornem strings formatadas diretamente  
- Integrar com sistemas de teste de formulários ou validação  

---

## Licença

MIT License