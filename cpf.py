import random

def geraCpf():
    
    cpf = [random.randint(0, 9) for _ in range(9)]

    soma = sum([i * v for i, v in enumerate(cpf[:9], start=1)])
    d1 = (soma % 11) % 10

    cpf.append(d1)

    soma = sum([i * v for i, v in enumerate(cpf[:10], start=0)])
    d2 = (soma % 11) % 10

    cpf.append(d2)

    cpfStr = ''.join(map(str, cpf))
    return f"{cpfStr[:3]}.{cpfStr[3:6]}.{cpfStr[6:9]}-{cpfStr[9:]}"

print("CPF geraado, segue ele logo abaixo:")
print(geraCpf())
