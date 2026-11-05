student('Arun', 'CSE', 21).
student('Bala', 'IT', 22).
student('Chitra', 'CSE', 20).
student('Divya', 'ECE', 21).

students_in_department(Department, Students) :-
    findall(Name, student(Name, Department, _), Students).

students_above_age(Limit, Students) :-
    findall(student(Name, Department, Age),
            (student(Name, Department, Age), Age > Limit),
            Students).

main :-
    students_in_department('CSE', CSEStudents),
    format('Students in CSE: ~w~n', [CSEStudents]),
    students_above_age(21, OlderStudents),
    format('Students above age 21: ~w~n', [OlderStudents]).

% Example queries:
% ?- students_in_department('CSE', Students).
% ?- students_above_age(20, Students).