fact(ravi_studies).

inference_rule([ravi_studies], ravi_gains_knowledge).
inference_rule([ravi_gains_knowledge], ravi_passes_examination).

all_known([], _).
all_known([Fact | Rest], Facts) :-
    memberchk(Fact, Facts),
    all_known(Rest, Facts).

derive(Facts, Closure) :-
    findall(Conclusion,
        (inference_rule(Premises, Conclusion),
         all_known(Premises, Facts),
         \+ memberchk(Conclusion, Facts)),
        NewFacts),
    (   NewFacts = []
    ->  Closure = Facts
    ;   append(Facts, NewFacts, Expanded),
        sort(Expanded, UniqueFacts),
        derive(UniqueFacts, Closure)
    ).

main :-
    derive([ravi_studies], Closure),
    (memberchk(ravi_passes_examination, Closure)
        -> writeln('Proved: Ravi passes the examination.')
        ;  writeln('Could not prove that Ravi passes the examination.')).

% Rules fire repeatedly until no new facts can be derived.