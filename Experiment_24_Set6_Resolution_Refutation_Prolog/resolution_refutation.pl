% Literals are terms; negated literals are wrapped as neg(Atom).
knowledge_base([
    [neg(human(Person)), mortal(Person)],
    [human(socrates)]
]).

complement(neg(Literal), Literal).
complement(Literal, neg(Literal)) :- Literal \= neg(_).

resolve_pair(First, Second, Resolvent) :-
    select(Literal, First, FirstRest),
    complement(Literal, Opposite),
    select(Opposite, Second, SecondRest),
    append(FirstRest, SecondRest, Combined),
    sort(Combined, Resolvent).

resolution_refutation(Clauses) :- saturate(Clauses, []).

saturate(Clauses, Seen) :-
    findall(Resolvent,
        ( select(First, Clauses, Others),
          member(Second, Others),
          copy_term((First, Second), (FreshFirst, FreshSecond)),
          resolve_pair(FreshFirst, FreshSecond, Resolvent),
          \+ memberchk(Resolvent, Clauses),
          \+ memberchk(Resolvent, Seen)
        ),
        Generated),
    sort(Generated, NewClauses),
    (   memberchk([], NewClauses)
    ->  true
    ;   NewClauses \= []
    ->  append(Clauses, NewClauses, Expanded),
        saturate(Expanded, NewClauses)
    ).

main :-
    knowledge_base(Knowledge),
    append(Knowledge, [[neg(mortal(socrates))]], RefutationClauses),
    (   resolution_refutation(RefutationClauses)
    ->  writeln('Resolution derived the empty clause: Socrates is mortal.')
    ;   writeln('Resolution could not prove the query.')
    ).

% Clauses: human(X) -> mortal(X); human(socrates); and the negated goal.