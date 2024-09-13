from classes.subject import find_student_registered_in_subject

def main():
    # Test: Estudiantes registrados
    print(find_student_registered_in_subject("Daniel", "Matematica"))  # True
    print(find_student_registered_in_subject("Daniel", "Biologia"))    # False
    
    # Test: Estudiante no registrado
    print(find_student_registered_in_subject("Juan", "Matematica"))    # False - Error message

if __name__ == "__main__":
    main()
