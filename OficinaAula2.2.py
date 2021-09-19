# Oficina Microlearning 7
# Introdução à Lógica de Programação em Python

cursos = [
  'Engenharia de Software',
  'Python para Data Science',
  'Introdução a Java'
]

respostas = [
    1, 2, 0, 1, 1, 1, 1, 0, 0, 2,
    2, 0, 1, 1, 1, 1, 2, 0, 1, 1,
    0, 1, 0, 2, 1, 1, 0, 2, 2, 1,
    0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]

total_votos = len(respostas)

votos_por_curso = [0, 0, 0]

for voto in respostas:
    if voto == 0:
        votos_por_curso[0] += 1
    elif voto == 1:
        votos_por_curso[1] += 1
    elif voto == 2:
        votos_por_curso[2] += 1

print(f'A quatidade de votos foi: {total_votos} votos\n\n')

for index in range(len(cursos)):
    percertual = (votos_por_curso[index]/total_votos)*100
    print(f'O curso {cursos[index]} obteve:'.ljust(42), end="")
    print(f'{votos_por_curso[index]} votos - {percertual:.2f}% do total.')

curso_ganhador = cursos[votos_por_curso.index(max(votos_por_curso))]

print(f'\n\n\tO curso mais votado foi: {curso_ganhador}\n\n')
