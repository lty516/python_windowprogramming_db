1. 필용한 라이브러리
	1) Tkinter : 기본 내장된 라이브러리
	2) wxPython
	3) PyQt
	...

2. 라이브러리 준비
    1) http://wxpython.org/Phoenix/snapshot-builds
            >	wxPython-4.1.1a1.dev4952+e5021fb5-cp37-cp37m-win_amd64.whl	2020-09-11 03:23	17M
            - 다운로드 받은 파일의 확장자를 zip으로 수정하고 압축을 풀어준다.
                wx폴더를 파이썬 설치폴더/lib/site-package 에 복사
            - 다운로드 받은 파일(.whl) 위치에서 콘솔창을 열고 아래와 같이 명령을 실행
                pip install 파일명
    2) 개발툴이 pycharm일 경우
            - File > Settings > Project:프로젝트명 > Progject Interpreterexit
                + 버튼을 누르고 설치하고자 하는 라이브러리 검색 후 install package 버튼 클릭

3. Layout Manager
    1) Sizer 클래스
        - 각각의 시각적 요소에 대한 적절한 크기를 계산
        - 특정 규칙에 따라 요소를 배치
        - 프레임의 크기를 조정할 때 동적으로 요소의 위치를 변경
    2) 구현 클래스
        - wx.Boxsizer : 가로 또는 세로로 컨트롤을 배치
        - wx.GridSizer : 그리드와 같은 구조로 컨트롤을 배치
        - wx.FlexGridSizer

4. Window Design Tool : wxFormBuilder
    1) https://sourceforge.net/projects/wxformbuilder/files/latest/download

5. 실행파일로 만들기
        cd (주소)
        pyinstaller -F --noconsole test7.py --hidden-import [wx]

6. DB 연동
    1) Sqlite
    2) MySQL
        create database pywin

        create table product(code int primary key,
                    product_name varchar(20),
                    product_count int,
                    product_price int);

                insert into product values(1,'장갑',3,5000);
                insert into product values(2,'가죽장갑',10,50000);
                insert into product values(3,'가죽점퍼',5,650000);

                create table Departure(buser_no int(4)  primary key,
                  dep_name varchar(10) not null,
                  dep_loc varchar(10),
                  dep_tel varchar(15));

                insert into Departure values(10,'총무부','서울','02-100-1111');
                insert into Departure values(20,'영업부','서울','02-100-2222');
                insert into Departure values(30,'전산부','서울','02-100-3333');

                create table emp(emp_no int(4) primary key,
                  emp_name varchar(10) not null,
                  dep_num int(4) not null,
                  emp_jik varchar(10) default '사원',
                  emp_pay int, sawon_ibsail date,
                  emp_gen char(3),
                  CONSTRAINT ck_sawon_gen check(sawon_gen='남' or sawon_gen='여'));

                insert into emp values(1,'홍길동',10,'사장',8000,'98/09/01','남');
                insert into emp values(2,'한국남',20,'부장',6200,'01/01/03','남');
                insert into emp values(3,'이순신',20,'과장',4500,'01/03/03','남');
                insert into emp values(4,'이미라',30,'대리',3503,'04/01/04','여');
                insert into emp values(5,'이순라',20,'사원',2850,'09/08/05','여');

                create table customer(cus_no int(4) primary key,
                  cus_name varchar(10) not null,
                  cus_tel varchar(20),
                  cus_jumin char(14),
                  cus_damsano int(4),
                  CONSTRAINT FK_gogek_damsano foreign key(gogek_damsano)
                  references sawon(sawon_no));

                insert into customer values(1,'이나라','02-535-2580','850612-1156789',1);
                insert into customer values(2,'김혜순','02-375-6946','700101-1054225',3);
                insert into customer values(3,'최부자','02-692-8926','890305-1065773',3);
                insert into customer values(4,'김해자','032-393-6277','770412-2028677',1);
                insert into customer values(5,'차일호','02-294-2946','790509-1062677',2);