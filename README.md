# Projeto: Calculadora em Shell Script e Python

## 📌 Sobre o projeto

Este projeto apresenta duas calculadoras simples desenvolvidas para praticar conceitos fundamentais de programação e automação no Ubuntu:

- **Calculadora em Shell Script (`calculadora.sh`)**
- **Calculadora em Python (`Calculadora.ipynb` ou `calculadora.py`)**

As duas versões permitem que o usuário informe dois números, escolha uma operação matemática e visualize o resultado no terminal ou no Jupyter Notebook.

Este projeto é útil para estudantes de Ciência de Dados porque trabalha conceitos básicos que também são utilizados em projetos maiores, como:

- Entrada e tratamento de dados;
- Conversão de tipos;
- Operadores matemáticos;
- Estruturas condicionais;
- Validação de dados;
- Interação com o usuário;
- Execução de programas no terminal Linux.

---

## 📁 Estrutura do projeto

```text
projeto-calculadora/
│
├── calculadora.sh
├── Calculadora.ipynb
└── README.md
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `calculadora.sh` | Calculadora desenvolvida em Shell Script para execução no terminal Ubuntu. |
| `Calculadora.ipynb` | Notebook Jupyter contendo a calculadora desenvolvida em Python. |
| `README.md` | Documentação e instruções do projeto. |

---

# 🐧 Calculadora em Shell Script

## Como funciona o arquivo `calculadora.sh`

O arquivo inicia com:

```bash
#!/bin/bash
```

Essa linha informa ao sistema que o script deve ser executado utilizando o interpretador Bash.

Em seguida, o programa exibe o título da calculadora:

```bash
echo "==== CALCULADORA ===="
```

O comando `echo` é utilizado para mostrar informações no terminal.

## Entrada dos números

```bash
read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2
```

O comando `read` recebe informações digitadas pelo usuário.

Os valores são armazenados nas variáveis:

- `num1`
- `num2`

## Menu de operações

O programa apresenta quatro opções:

```text
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
```

Depois, a opção escolhida é armazenada na variável `opcao`.

## Estrutura `case`

O comando `case` verifica qual opção foi escolhida pelo usuário:

```bash
case $opcao in
```

Cada número executa uma operação diferente:

- `1`: soma;
- `2`: subtração;
- `3`: multiplicação;
- `4`: divisão;
- qualquer outro valor: opção inválida.

## Operações matemáticas

No Shell Script, as operações são realizadas utilizando a estrutura:

```bash
resultado=$((num1 + num2))
```

O símbolo `$(( ))` permite realizar cálculos aritméticos no Bash.

## Validação da divisão por zero

Antes de realizar a divisão, o programa verifica se o segundo número é igual a zero:

```bash
if [ "$num2" -eq 0 ]; then
    echo "Erro: divisão por zero não é permitida."
fi
```

Essa verificação evita um erro matemático durante a execução.

> A versão atual do Shell Script trabalha com números inteiros. Por isso, uma divisão como `5 / 2` retorna `2`, sem casas decimais.

---

# ▶️ Como executar a calculadora `.sh`

## 1. Abrir o terminal

No Ubuntu ou WSL, abra o terminal.

## 2. Acessar a pasta do arquivo

Utilize o comando `cd`:

```bash
cd caminho/da/pasta
```

Exemplo:

```bash
cd ~/projetos/automacoes_python
```

## 3. Verificar se o arquivo está na pasta

```bash
ls
```

O arquivo `calculadora.sh` deverá aparecer na lista.

## 4. Dar permissão de execução

```bash
chmod +x calculadora.sh
```

Esse comando torna o arquivo executável.

## 5. Executar a calculadora

```bash
./calculadora.sh
```

Também é possível executar sem alterar a permissão:

```bash
bash calculadora.sh
```

## Exemplo de uso

```text
==== CALCULADORA ====
Digite o primeiro número: 20
Digite o segundo número: 5

Escolha a Operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão

Opção: 4
Resultado: 4
```

---

# 🐍 Calculadora em Python

## Como funciona o arquivo Python

A versão em Python começa exibindo o nome do programa:

```python
print("Calculadora em Python")
```

## Entrada e conversão dos números

```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
```

O comando `input()` recebe os valores digitados pelo usuário.

Como o `input()` retorna texto, a função `float()` converte os valores para números decimais.

Isso permite trabalhar com valores como:

```text
10
5.5
7.25
```

## Escolha da operação

```python
opcao = input("Digite o número da operação desejada: ")
```

A escolha do usuário é armazenada como texto.

Por isso, o programa compara a opção utilizando valores entre aspas, como `"1"` e `"2"`.

## Estrutura condicional

O programa utiliza:

```python
if
elif
else
```

Essas estruturas verificam qual operação foi escolhida.

### Soma

```python
if opcao == "1":
    resultado = num1 + num2
```

### Subtração

```python
elif opcao == "2":
    resultado = num1 - num2
```

### Multiplicação

```python
elif opcao == "3":
    resultado = num1 * num2
```

### Divisão

```python
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
```

Antes da divisão, o programa verifica se `num2` é diferente de zero.

## Opção inválida

```python
else:
    print("Opção inválida.")
```

Caso o usuário escolha um número diferente de 1, 2, 3 ou 4, o programa informa que a opção é inválida.

---

# ▶️ Como executar a calculadora em Python

## Opção 1: Jupyter Notebook

Abra o Jupyter Notebook:

```bash
jupyter notebook
```

Depois:

1. Abra o arquivo `Calculadora.ipynb`;
2. Selecione a célula de código;
3. Pressione `Shift + Enter`;
4. Informe os números e a operação desejada.

## Opção 2: Google Colab

1. Acesse o Google Colab;
2. Clique em **Arquivo**;
3. Selecione **Fazer upload de notebook**;
4. Envie o arquivo `Calculadora.ipynb`;
5. Execute a célula.

## Opção 3: Arquivo `.py`

O código do notebook também pode ser salvo como:

```text
calculadora.py
```

Depois, execute no terminal:

```bash
python3 calculadora.py
```

## Exemplo de uso

```text
Calculadora em Python
Digite o primeiro número: 15.5
Digite o segundo número: 2

Escolha uma operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão

Digite o número da operação desejada: 3
Resultado da multiplicação: 31.0
```

---

# 🔄 Comparação entre as versões

| Característica | Shell Script | Python |
|---|---|---|
| Execução | Terminal Ubuntu/WSL | Terminal, Jupyter ou Colab |
| Números decimais | Não na versão atual | Sim |
| Estrutura de decisão | `case` e `if` | `if`, `elif` e `else` |
| Entrada de dados | `read` | `input()` |
| Exibição de resultados | `echo` | `print()` |
| Divisão por zero | Validada | Validada |

---

# 🧠 Conceitos praticados

Neste projeto foram utilizados:

- Variáveis;
- Entrada de dados;
- Conversão de tipos;
- Operadores matemáticos;
- Estruturas condicionais;
- Menu de opções;
- Validação de divisão por zero;
- Execução de scripts no Ubuntu;
- Uso do terminal;
- Programação em Python;
- Automação com Shell Script.

---

# 🚀 Possíveis melhorias

O projeto pode ser ampliado com:

- Laço de repetição para realizar várias operações;
- Opção para encerrar o programa;
- Validação para impedir letras no lugar de números;
- Cálculo de potência;
- Cálculo de raiz quadrada;
- Porcentagem;
- Histórico de operações;
- Interface gráfica;
- Testes automatizados;
- Suporte a números decimais no Shell Script.

---

# 👨‍💻 Autor

**ELIAS RAMINELI**

Projeto desenvolvido para praticar Python, Linux, Shell Script e fundamentos importantes para a formação em Analista de Dados pela EBAC.
