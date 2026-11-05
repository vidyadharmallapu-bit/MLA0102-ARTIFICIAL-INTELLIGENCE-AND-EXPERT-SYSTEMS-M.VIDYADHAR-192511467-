bird(parrot).
healthy(parrot).

can_fly(Animal) :- bird(Animal).

main :-
    (can_fly(parrot)
        -> writeln('Proved by backward chaining: Parrot can fly.')
        ;  writeln('Could not prove that Parrot can fly.')),
    (healthy(parrot) -> writeln('Parrot is healthy.') ; true).

% Query: ?- can_fly(parrot).