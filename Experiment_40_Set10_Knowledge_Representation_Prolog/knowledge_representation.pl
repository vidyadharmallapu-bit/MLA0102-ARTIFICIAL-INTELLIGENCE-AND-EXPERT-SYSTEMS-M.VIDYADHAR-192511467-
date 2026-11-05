studies_ai(kumar).

learns_intelligent_systems(Student) :- studies_ai(Student).
can_solve_ai_problems(Student) :- learns_intelligent_systems(Student).

main :-
    (can_solve_ai_problems(kumar)
        -> writeln('Proved: Kumar can solve AI problems.')
        ;  writeln('Could not prove that Kumar can solve AI problems.')).

% Query: ?- can_solve_ai_problems(kumar).