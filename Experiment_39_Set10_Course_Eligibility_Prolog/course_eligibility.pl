student_marks('Kumar', 82, 91, 76).
student_marks('Leela', 58, 64, 70).
student_marks('Manoj', 45, 80, 60).

course_requirement(ai, 60, 60, 55, 180).

eligible(Student, Course) :-
    student_marks(Student, Mathematics, Programming, English),
    course_requirement(Course, MinimumMath, MinimumProgramming, MinimumEnglish, MinimumTotal),
    Mathematics >= MinimumMath,
    Programming >= MinimumProgramming,
    English >= MinimumEnglish,
    Total is Mathematics + Programming + English,
    Total >= MinimumTotal.

main :-
    forall(student_marks(Student, _, _, _),
        (eligible(Student, ai)
            -> format('~w is eligible for AI.~n', [Student])
            ;  format('~w is not eligible for AI.~n', [Student]))).

% Eligibility cutoffs are illustrative and can be changed in course_requirement/5.
% Query: ?- eligible(Student, ai).