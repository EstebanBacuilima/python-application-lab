from classes.subject import find_student_registered_in_subject

def main():
    # Test: Estudiantes registrados
    print(find_student_registered_in_subject("Daniel", "Matematica"))  # Debería ser True
    print(find_student_registered_in_subject("Daniel", "Biologia"))    # Debería ser False
    
    # Test: Estudiante no registrado
    print(find_student_registered_in_subject("Juan", "Matematica"))    # Debería ser False y mensaje de error

if __name__ == "__main__":
    main()
