road(chennai, bengaluru).
road(bengaluru, hyderabad).
road(hyderabad, delhi).
road(chennai, mumbai).
road(mumbai, delhi).
road(bengaluru, mumbai).

connected_city(City1, City2) :- road(City1, City2).
connected_city(City1, City2) :- road(City2, City1).

route(Start, Goal, Path) :-
    travel(Start, Goal, [Start], ReversePath),
    reverse(ReversePath, Path).

travel(Goal, Goal, Visited, Visited).
travel(Current, Goal, Visited, Path) :-
    connected_city(Current, Next),
    \+ memberchk(Next, Visited),
    travel(Next, Goal, [Next | Visited], Path).

main :-
    (   route(chennai, delhi, Path)
    ->  write('Path from chennai to delhi: '),
        print_path(Path)
    ;   writeln('No route found.')
    ).

print_path([City]) :-
    format('~w~n', [City]).
print_path([City | Rest]) :-
    format('~w -> ', [City]),
    print_path(Rest).

% Example query: ?- route(chennai, delhi, Path).