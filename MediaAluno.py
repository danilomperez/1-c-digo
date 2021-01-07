def media_notas(nota1, nota2, nota3, nota4):
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4

    print(f'A soma das notas é: {soma}')
    if media >= 6:
        print(f'O aluno {nome_aluno} foi aprovado com a nota final:{media}')
    elif media == 5 or media ==4:
        print(f'O aluno {nome_aluno} ficou de recuperação, nota final: {media}')
    if media<=3:
        print(f'O aluno {nome_aluno} foi reprovado direto, nota final: {media}')
    return media


nome_aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))


media = media_notas (n1, n2, n3, n4)
