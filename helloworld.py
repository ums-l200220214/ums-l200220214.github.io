class Student:
    def __init__(self, name):
        self.name = name
        self.spp_paid = False
        self.grades = []

    def pay_spp(self):
        self.spp_paid = True
        print(f"{self.name} telah membayar SPP.")

    def enroll_course(self, course):
        if not self.spp_paid:
            print(f"{self.name} tidak bisa mendaftar ke mata kuliah {course} sebelum membayar SPP.")
        else:
            print(f"{self.name} telah mendaftar ke mata kuliah {course}.")

    def submit_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name} telah mendapatkan nilai {grade}.")

    def calculate_final_grade(self):
        if not self.grades:
            return 0
        final_grade = sum(self.grades) / len(self.grades)
        return final_grade

    def display_final_grade(self):
        final_grade = self.calculate_final_grade()
        print(f"Nilai akhir {self.name} adalah {final_grade:.2f}.")


def main():
    # Membuat objek student
    student1 = Student("Ali")

    # Proses pembayaran SPP
    student1.pay_spp()

    # Mendaftar ke mata kuliah
    student1.enroll_course("Pemrograman Dasar")
    student1.enroll_course("Algoritma dan Struktur Data")

    # Mengumpulkan nilai
    student1.submit_grade(85)
    student1.submit_grade(90)

    # Menampilkan nilai akhir
    student1.display_final_grade()


if __name__ == "__main__":
    main()
