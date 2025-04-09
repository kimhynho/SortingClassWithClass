
#프로그램명: SortingClassWithClass.py
#작성자: 소웨 김현호
#작성일: 4/10
#프로그램 설명: 학생 성적 관리 프로그램 이 프로그램은 학생들의 성적을 입력받고, 총점/평균/학점을 계산해서 출력합니다.
#또한 등수 계산, 성적 삭제, 검색, 총점등이 가능, 리스트 버전에서 클래로 변경했습니다.
#기능 요약 성적 입력,성적 출력,등수 계산,성적 삭제, 학생 검색, 총점으로 정렬, 평균 80점 이상 학생 수 확인
 
# 학생 클래스 (이름, 성적 이런 거 저장할려고 만듬)
class Student:
    def __init__(self, hakbun, name, eng, c, py):
        self.hakbun = hakbun
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.total = eng + c + py  # 총점
        self.avg = self.total / 3  # 평균
        self.grade = self.get_grade()  # 학점
        self.rank = 0  # 등수는 나중에 계산함

    def get_grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"{self.hakbun}\t{self.name}\t{self.eng}\t{self.c}\t{self.py}\t{self.total}\t{self.avg:.1f}\t{self.grade}\t{self.rank}"


# 전체 학생 관리하는 클래스임 (리스트에 다 넣어놓고 관리)
class StudentManager:
    def __init__(self):
        self.students = []

    def input_score(self):
        print("== 학생 정보 입력 ==")
        hakbun = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c = int(input("C언어 점수: "))
        py = int(input("파이썬 점수: "))
        s = Student(hakbun, name, eng, c, py)
        self.students.append(s)
        print("입력 완료 \n")

    def print_all(self):
        print("학번\t이름\t영어\tC\t파이썬\t총점\t평균\t학점\t등수")
        for s in self.students:
            print(s)

    def calc_rank(self):
        sorted_list = sorted(self.students, key=lambda x: x.total, reverse=True)
        for idx, stu in enumerate(sorted_list):
            stu.rank = idx + 1  # 등수는 1등부터 시작
        print("등수 계산됨 \n")

    def delete_student(self):
        target = input("삭제할 학생 학번 입력: ")
        for i, s in enumerate(self.students):
            if s.hakbun == target:
                del self.students[i]
                print("삭제 완료!")
                return
        print("그런 학번 없음")

    def search_student(self):
        key = input("학번이나 이름으로 검색: ")
        for s in self.students:
            if s.hakbun == key or s.name == key:
                print("찾음")
                print("학번\t이름\t영어\tC\t파이썬\t총점\t평균\t학점\t등수")
                print(s)
                return
        print("못찾음")

    def sort_total(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        self.calc_rank()
        self.print_all()

    def count_over_80(self):
        cnt = 0
        for s in self.students:
            if s.avg >= 80:
                cnt += 1
        print("평균 80점 넘는 사람:", cnt, "명")


# 메뉴 선택하는 메인 함수임 (while문으로 반복됨)
def main():
    manager = StudentManager()
    while True:
        print("\n====== 학생 성적 관리 ======")
        print("1. 성적 입력")
        print("2. 전체 출력")
        print("3. 등수 계산")
        print("4. 성적 삭제")
        print("5. 학생 검색")
        print("6. 총점 정렬")
        print("7. 평균 80점 넘는 사람 몇명인지 보기")
        print("8. 종료")

        choice = input("번호 고르셈: ")
        if choice == '1':
            manager.input_score()
        elif choice == '2':
            manager.print_all()
        elif choice == '3':
            manager.calc_rank()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.search_student()
        elif choice == '6':
            manager.sort_total()
        elif choice == '7':
            manager.count_over_80()
        elif choice == '8':
            print("종료")
            break
        else:
            print("잘못 누름")


if __name__ == "__main__":
    main()
