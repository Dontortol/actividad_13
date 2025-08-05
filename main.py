students = {'123': {'name': 'Rodrigo', 'carrer': 'Correr'}, '555': {'name': 'Yhibra', 'carrer': 'Gay'}}
courses = {'123':{}, '555':{}}
def add_student():
    while True:
        id = input("Ingresa el codigo del estudiante: ").upper()
        if id not in students:
            break
        else:
            print("El codigo de estudiante ya existe")
    name = input("Ingresa nombre completo del estudiante: ").capitalize()
    carrer = input("Ingresa el carrera del estudiante: ").capitalize()
    courses[id] = {}
    students[id] = {
        "name": name,
        "carrer": carrer
    }
def add_course():
    searc_code = input("Ingresa el codigo del estudiante: ")
    if not searc_code in students:
        print("El codigo de estudiante no existe")
    else:
        while True:
            print("1. Ingresar nuevo curso\n"
                  "2. Regresar al menu")
            chose = input("Ingrese la opcion deseada: ")
            match chose:
                case "1":
                    try:
                        course_amount = int(input("Ingresa el numero de cursos que quiera ingresar: "))
                    except ValueError:
                        print("Debe ser un numero entero: ")
                    except Exception as e:
                        print("Error inesperado",e)
                    else:
                        for i in range(course_amount):
                            course = input("Ingresa el nombre del curso: ")
                            while True:
                                try:
                                    note = int(input("Ingresa el nota del curso: "))
                                    if note < 0 or note > 100:
                                        print("La nota debe ser entre 0 a 100 puntos")
                                    else:
                                        print("Curso agregado")
                                        courses[searc_code][course] = note
                                        break
                                except ValueError:
                                    print("Debe ser un numero entero")
                                except Exception as e:
                                    print("Error inesperado",e)
                case "2":
                    print("Regresando al menu")
                    break
                case _:
                    print("Debe ser una opcion valida")

def consult_students():
    searc_code = input("Ingresa el codigo del estudiante: ").upper()
    if not searc_code in students:
        print("El codigo de estudiante ingresado no existe")
    else:
        for id_s, value in students.items():
            if id_s == searc_code:
                print(f">Codigo unico: {id_s}\n"
                      f">Nombre del estudiante: {value['name']}\n"
                      f">Carrera: {value['carrer']}")
                if not courses:
                    print("sin cursos asignados")
                else:
                    for id_c, value_c in courses.items():
                        if id_c == searc_code:
                            print(f"----Cursos del estudiante----")
                            print(f"Nombre del curso: {value_c}\n")
    print(students)
    print(courses)



while True:
    print("--Bienvenido al sistema de gestion academica--\n"
          "1. Agregar estudiante\n"
          "2. Agregar curso y nota\n"
          "3. Consultar estudiante\n"
          "4. Calcular promedio del estudiante\n"
          "5. Verificar si aprueba\n"
          "6. Mostrar estudiantes\n"
          "7. Salir")
    select = input("Ingrese una de las siguientes opciones: ")
    match select:
        case "1":
            add_student()
        case "2":
            if not students:
                print("Aun no hay estudiantes")
            else:
                add_course()
        case "3":
            if not students:
                print("Aun no hay estudiantes")
            else:
                consult_students()
        case "7":
            print("Saliendo del sistema")
            break
        case _:
            print("Debe ser una opcion valida")