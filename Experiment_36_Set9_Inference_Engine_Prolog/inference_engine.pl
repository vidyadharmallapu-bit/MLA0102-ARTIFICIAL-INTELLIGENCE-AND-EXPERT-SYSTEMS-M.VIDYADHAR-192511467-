% Add fact/1 and rule/2 clauses to extend the knowledge base.
fact(human(socrates)).
rule(mortal(Person), [human(Person)]).

prove(Goal) :- prove(Goal, []).
prove(Goal, _) :- fact(Goal).
prove(Goal, Seen) :-
    \+ memberchk(Goal, Seen),
    rule(Goal, Premises),
    prove_all(Premises, [Goal | Seen]).

prove_all([], _).
prove_all([Goal | Rest], Seen) :-
    prove(Goal, Seen),
    prove_all(Rest, Seen).

main :-
    Query = mortal(socrates),
    (prove(Query) -> format('Proved: ~w~n', [Query])
        ; format('Could not prove: ~w~n', [Query])).

% Example: fact(bird(parrot)).
%          rule(can_fly(Animal), [bird(Animal)]).
% Then query: ?- prove(can_fly(parrot)).