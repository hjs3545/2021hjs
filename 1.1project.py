import unittest

# 딕셔너리정의
학생부 = {20211: ['황재성', '인공지능학과'], 20212: ['심태완', '컴퓨터융합학부'],
       20213: ['전승주', '기계공학과'], 20214: ['유채민', '화학과']}

교실 = {20211: '201호', 20212: '202호', 20213: '203호', 20214: '204호'}

L1 = []  # 정상 온도 모교리스트
L2 = []  # 정상 온도 외부리스트
L3 = []  # 고열 환자 모교리스트
L4 = []  # 고열 환자 외부리스트


# 37도 이상 리스트 함수
def over():  # a=학번,b=이름,c=학과
    """학번 a는 5자리 정수, 외부인일때 학번에 0 입력"""
    print("학번을 입력하세요.(외부인코드=0)")
    a = int(input())
    try:
        (len(str(a)) / (len(str(a)) - 5)) and (len(str(a)) / (len(str(a)) - 1))
    except:
        print("이름을 입력하세요.")
        b = input()
        if (a != 0):
            print("학과를 입력하세요.")
            c = input()
        global L3
        global L4
        if a in 학생부:
            L3.append((a, b, c))
            for i in range(len(L3)):
                if L3[i][0] in list(학생부.keys()):
                    print("(고열의심)우리학교 학생입니다.")
                    print(학생부.get(L3[i][0]))
                    print("시험실" + 교실[a] + "로 이동해주세요.")
        else:
            L4.append(b)
            print("(고열의심)우리학교 학생이 아닙니다.")

        return
    else:
        print("학번 a는 5자리 정수,외부인일때 학번에 0 입력")
        over()


# 정상온도 출입명부작성 함수
def checkin():  # a=학번,b=이름,c=학과
    """학번 a는 5자리 정수,외부인일때 학번에 0 입력"""
    print("학번을 입력하세요.(외부인코드=0)")
    a = int(input())
    try:
        (len(str(a)) / (len(str(a)) - 5)) and (len(str(a)) / (len(str(a)) - 1))
    except:
        print("이름을 입력하세요.")
        b = input()
        if (a != 0):
            print("학과를 입력하세요.")
            c = input()

        global L1
        global L2
        if a in 학생부:
            L1.append((a, b, c))
            for i in range(len(L1)):
                if L1[i][0] in list(학생부.keys()):
                    print("(정상온도)우리학교 학생입니다.")
                    print(학생부.get(L1[i][0]))
                    print("시험실" + 교실[a] + "로 이동해주세요.")
        else:
            L2.append(b)
            print("(정상온도)우리학교 학생이 아닙니다.")

        return
    else:
        print("학번 a는 5자리 정수,외부인일때 학번에 0 입력")
        checkin()


help(over)
help(checkin)

# 첫번째 온도 체크
"""양의 값을 입력하세요."""
print("온도를 체크합니다.")
X = int(input())
if X < 0:
    raise ValueError("양의 값을 입력하세요.")

if X >= 37:
    over()
elif 0 < X < 37:
    checkin()
print("온도를 체크할 사람이 더 있습니까?(있음,없음)")
d = input()

# 입구 온도 체크 무한루프

while (d == "있음"):
    print("온도를 체크합니다.")
    X = int(input())
    if X >= 37:
        over()
    elif 0 < X < 37:
        checkin()
    print("온도를 체크할 사람이 더 있습니까?(있음,없음)")
    d = input()

print("============================================================")
print("정상온도 모교리스트")
print(L1)
print("고열환자 모교리스트")
print(L3)
print("정상온도 외부리스트")
print(L2)
print("고열환자 외부리스트")
print(L4)
print("============================================================")

"""
# 학생부Dictionary의 key , value 매치확인
class TestDict(unittest.TestCase):
    def test_dict(self):
        self.assertEqual(학생부[20212], ['심태완', '컴퓨터융합학부'], "False!")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


class Testdictclass(unittest.TestCase):

    def test_dictclass(self):
        self.assertEqual(교실[20211], '201호', "False")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# over,checkin 함수 unittest

import unittest

# 딕셔너리정의
학생부 = {20211: ['황재성', '인공지능학과'], 20212: ['심태완', '컴퓨터융합학부'],
       20213: ['전승주', '기계공학과'], 20214: ['유채민', '화학과']}

교실 = {20211: '201호', 20212: '202호', 20213: '203호', 20214: '204호'}

L1=[] #정상 온도 모교리스트
L2=[] #정상 온도 외부리스트
L3=[] #고열 환자 모교리스트
L4=[] #고열 환자 외부리스트


def overTest(a,b,c):  # a=학번,b=이름,c=학과
    global L3
    global L4
    if a in 학생부:
        L3.append((a, b, c))
        for i in range(len(L3)):
            if L3[i][0] in list(학생부.keys()):
                return "(고열의심)우리학교 학생입니다."
    else:
        L4.append(b)
        return "(고열의심)우리학교 학생이 아닙니다."



def checkinTest(a,b,c):  # a=학번,b=이름,c=학과
    global L1
    global L2
    if a in 학생부:
        L1.append((a, b, c))
        for i in range(len(L1)):
            if L1[i][0] in list(학생부.keys()):
                return "(정상온도)우리학교 학생입니다."

    else:
        L2.append(b)
        return "(정상온도)우리학교 학생이 아닙니다."


# over함수 unittest
class TestOver(unittest.TestCase):
    def test_over1(self):
        self.assertEqual(overTest(20211, '황재성', '인공지능학과'), '(고열의심)우리학교 학생입니다.', "False")
        self.assertIn((20211, '황재성', '인공지능학과'), L3)
    def test_over2(self):
        self.assertEqual(overTest(0, '김민호', 'X'), '(고열의심)우리학교 학생이 아닙니다.', "False")
        self.assertIn('김민호', L4)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# checkin함수 unittest
class TestCheckin(unittest.TestCase):
    def test_checkin1(self):
        self.assertEqual(checkinTest(20212, '심태완', '컴퓨터융합학부'), '(정상온도)우리학교 학생입니다.', "False")
        self.assertIn((20212, '심태완', '컴퓨터융합학부'), L1)

    def test_checkin2(self):
        self.assertEqual(checkinTest(0, '김민호','X'), '(정상온도)우리학교 학생이 아닙니다.', "False")
        self.assertIn('김민호', L2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)




"""