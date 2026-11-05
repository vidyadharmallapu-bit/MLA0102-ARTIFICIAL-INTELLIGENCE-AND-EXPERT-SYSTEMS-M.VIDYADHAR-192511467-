student(anu).
student(ben).
course(ai).
course(databases).
faculty('Dr Rao').
faculty('Dr Shah').
enrolled(anu, ai).
enrolled(ben, databases).
enrolled(anu, databases).
teaches('Dr Rao', ai).
teaches('Dr Shah', databases).

students_in_course(Course, Students) :-
    findall(Student, enrolled(Student, Course), Students).

main :-
    students_in_course(ai, Students),
    format('Students enrolled in AI: ~w~n', [Students]),
    (teaches(Faculty, ai) -> format('AI faculty: ~w~n', [Faculty]) ; true).

% Query: ?- students_in_course(databases, Students).