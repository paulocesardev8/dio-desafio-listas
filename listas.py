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
