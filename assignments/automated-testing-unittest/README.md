# 📘 Assignment: Automated Testing with unittest

## 🎯 Objetivo

Aprenda a verificar o comportamento de funções Python com testes automatizados usando o módulo `unittest` da biblioteca padrão. Pratique testes de casos comuns, valores-limite e leitura de falhas para localizar defeitos.

## 📝 Tarefas

### 🛠️ Escrever Testes para Casos Comuns

#### Descrição
Complete a classe `TestUtilityFunctions` no código inicial e escreva testes para as funções de soma e verificação de paridade.

#### Requisitos
O programa concluído deve:

- Usar `unittest.TestCase` para organizar os testes.
- Verificar resultados de `add_numbers()` com números positivos e negativos.
- Verificar que `is_even()` retorna `True` para números pares e `False` para ímpares.
- Executar os testes com `python3 starter-code.py`.

### 🛠️ Cobrir Valores-Limite e Entradas de Texto

#### Descrição
Amplie a suíte para cobrir valores que costumam revelar erros, incluindo zero, números negativos e nomes com espaços extras.

#### Requisitos
O programa concluído deve:

- Testar `add_numbers()` com zero e com pelo menos um número negativo.
- Testar `is_even()` com zero e com um número negativo.
- Testar se `normalize_name()` remove espaços no início e no fim e reduz espaços repetidos a um só.
- Confirmar que a normalização de uma string vazia retorna uma string vazia.

### 🛠️ Interpretar Falhas e Confirmar a Suíte

#### Descrição
Use o resultado dos testes para entender como uma falha aponta uma diferença entre o comportamento esperado e o código executado. Faça uma alteração temporária em uma função, execute os testes e depois restaure a implementação.

#### Requisitos
O programa concluído deve:

- Exibir uma falha ao alterar temporariamente uma implementação de modo que ela produza um resultado incorreto.
- Identificar no relatório qual teste falhou e qual era o valor esperado e o obtido.
- Restaurar a implementação original e executar novamente a suíte sem falhas.
