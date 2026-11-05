student(anu).
student(bala).
faculty('Dr Rao').
faculty('Dr Shah').
department(cse).
course(ai, cse).
course(databases, cse).
faculty_teaches('Dr Rao', ai).
faculty_teaches('Dr Shah', databases).
student_studies(anu, ai).
student_studies(bala, databases).

teacher_of(Course, Faculty) :- faculty_teaches(Faculty, Course).
students_studying(Course, Students) :-
    findall(Student, student_studies(Student, Course), Students).

main :-
    teacher_of(ai, Teacher),
    format('Faculty teaching AI: ~w~n', [Teacher]),
    students_studying(ai, Students),
    format('Students studying AI: ~w~n', [Students]).

% Queries: ?- teacher_of(databases, Faculty).
%          ?- students_studying(databases, Students).