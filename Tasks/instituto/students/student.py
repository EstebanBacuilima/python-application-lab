# Json students
student_list = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def get_subjects_by_student_name(student_name):
    try:
        return student_list[student_name]
    except KeyError:
        raise ValueError(f"El estudiante {student_name} no está registrado.")
