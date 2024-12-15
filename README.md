# dio-desafio-listas

# Explicação do Código: Elementos Comuns entre Duas Listas

Este documento descreve o funcionamento do código que identifica os elementos comuns entre duas listas de números fornecidas pelo usuário. Também inclui exemplos de execução e uma correção necessária para evitar erros.

---

## **Descrição do Código**

### **Função `elementos_comuns`**
- **Propósito**: Encontrar os elementos comuns entre duas listas de números fornecidas como strings.
- **Entrada**:
  - `lista1`: String contendo números separados por espaços.
  - `lista2`: String contendo números separados por espaços.
- **Processamento**:
  1. Converte as strings de entrada para conjuntos de inteiros usando `map(int, lista.split())`.
  2. Calcula a interseção entre os dois conjuntos usando `set1 & set2`.
  3. Converte o resultado da interseção para uma lista.
  4. Se houver um erro de conversão para inteiros (e.g., entradas inválidas), captura a exceção `ValueError` e retorna a mensagem `"Entrada inválida."`.
- **Saída**:
  - Uma lista contendo os elementos comuns entre as duas listas, ou a mensagem `"Entrada inválida."` em caso de erro.

**Exemplo de Uso**:
```python
elementos_comuns("1 2 3", "2 3 4")  # Retorna [2, 3]
elementos_comuns("a b c", "1 2 3")  # Retorna "Entrada inválida."
```

### **Função `main`**
- **Propósito**: Gerenciar a interação com o usuário.
- **Entrada**:
  1. Solicita duas strings de números separados por espaços fornecidas pelo usuário.
- **Processamento**:
  1. Chama a função `elementos_comuns` para encontrar os elementos comuns entre as listas fornecidas.
  2. Trata o caso de erro exibindo a mensagem "Entrada inválida." se for detectada uma exceção.
- **Saída**:
  - Exibe os elementos comuns no formato: `"Elementos comuns às duas listas: <resultado>"`.

### **Controle do Fluxo de Execução**
A linha:
```python
if _name_ == "_main_":
```
é usada para verificar se o arquivo está sendo executado diretamente. Contudo, está incorreta. A linha correta é:
```python
if __name__ == "__main__":
```

---

## **Código Corrigido**

```python
def elementos_comuns(lista1, lista2):
    try:
        # Converte as listas de strings para listas de inteiros
        set1 = set(map(int, lista1.split()))
        set2 = set(map(int, lista2.split()))
        
        # Encontra a interseção dos dois conjuntos
        interseccao = set1 & set2
        
        # Converte o resultado para uma lista e retorna
        return list(interseccao)
    except ValueError:
        return "Entrada inválida."

# Função principal para ler a entrada e exibir a saída
def main():
    # Lê as entradas do usuário
    entrada1 = input()
    entrada2 = input()
    
    # Obtém os elementos comuns
    resultado = elementos_comuns(entrada1, entrada2)
    
    # Exibe o resultado no formato especificado
    if resultado == "Entrada inválida.":
        print(resultado)
    else:
        print(f"Elementos comuns às duas listas: {resultado}")

# Chama a função principal
if __name__ == "__main__":
    main()
```

---

## **Exemplo de Execução**

### **Entrada**:
```
1 2 3
2 3 4
```

### **Processo**:
1. As strings de entrada `"1 2 3"` e `"2 3 4"` são convertidas em conjuntos:
   - `set1 = {1, 2, 3}`
   - `set2 = {2, 3, 4}`
2. Calcula-se a interseção: `set1 & set2 = {2, 3}`.
3. O resultado é convertido para uma lista: `[2, 3]`.

### **Saída**:
```
Elementos comuns às duas listas: [2, 3]
```

---

## **Resumo do Fluxo**
1. O usuário insere duas listas de números separados por espaços.
2. O programa converte as entradas em conjuntos de inteiros.
3. A função `elementos_comuns` calcula os elementos comuns (interseção) entre os dois conjuntos.
4. O resultado é exibido ao usuário.
5. Entradas inválidas são tratadas e geram a mensagem de erro apropriada.

---

## **Erros Corrigidos**
1. Substituído `_name_` e `_main_` por `__name__` e `__main__` para evitar erros de execução.
2. Adicionado tratamento para entradas inválidas com a exceção `ValueError`.

