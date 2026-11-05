marks('Ananya', 88, 82, 91).
marks('Kiran', 48, 72, 81).
marks('Meera', 60, 59, 70).

eligible(Person) :-
    marks(Person, Mathematics, Physics, ComputerScience),
    Mathematics >= 50,
    Physics >= 50,
    ComputerScience >= 50,
    Total is Mathematics + Physics + ComputerScience,
    Total >= 180.

main :-
    (eligible('Ananya') -> writeln('Ananya is eligible.') ; writeln('Ananya is not eligible.')),
    (eligible('Kiran') -> writeln('Kiran is eligible.') ; writeln('Kiran is not eligible.')),
    (eligible('Meera') -> writeln('Meera is eligible.') ; writeln('Meera is not eligible.')).

% Sample policy: at least 50 in each subject and at least 180 overall.
% Query: ?- eligible(Person).