estudiantes = {}
lista_suspensos = []
lista_aprobados = []
media = []
for num in range(1, 10+1):
    estudiantes[num] = {}
    nombre_estudiante = str(input("Introduzca nombre del alumno: "))
    nota_estudiante = float(input("Introduzca la nota del alumno: "))
    estudiantes[num]["Nombre"] = nombre_estudiante
    estudiantes[num]["Nota"] = nota_estudiante
    if nota_estudiante < 5:
        lista_suspensos.append(estudiantes[num]["Nombre"])
        media.append(estudiantes[num]["Nota"])
    else:
        lista_aprobados.append(estudiantes[num]["Nombre"])
        media.append(estudiantes[num]["Nota"])
print("Lista de estudiantes introducidas con sus notas")
print(estudiantes)
print("Lista de aprobados")
print(lista_aprobados)
print("Lista de suspendidos")
print(lista_suspensos)
print("Media total")
print(sum(media)/len(media))