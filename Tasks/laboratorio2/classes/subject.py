from students.student import get_subjects_by_student_name 

def find_student_registered_in_subject(nombre, materia):
    """Find if a student is registered in a subject"""
    try:
        subjects = get_subjects_by_student_name(nombre)
        return materia in subjects
    except ValueError:
        print(f"El estudiante {nombre} no está registrado.")
        return False
