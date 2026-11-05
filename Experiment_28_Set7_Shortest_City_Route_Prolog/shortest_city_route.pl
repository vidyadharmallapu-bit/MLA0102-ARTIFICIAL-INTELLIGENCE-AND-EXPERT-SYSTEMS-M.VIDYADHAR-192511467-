road(chennai, bengaluru, 350).
road(bengaluru, hyderabad, 570).
road(hyderabad, delhi, 1550).
road(chennai, mumbai, 1330).
road(mumbai, delhi, 1400).
road(bengaluru, mumbai, 980).

connected(A, B, Distance) :- road(A, B, Distance).
connected(A, B, Distance) :- road(B, A, Distance).

city_path(Start, Goal, Path, Distance) :-
    travel(Start, Goal, [Start], ReversePath, 0, Distance),
    reverse(ReversePath, Path).

travel(Goal, Goal, Visited, Visited, Distance, Distance).
travel(Current, Goal, Visited, Path, SoFar, Total) :-
    connected(Current, Next, Leg),
    \+ memberchk(Next, Visited),
    NewDistance is SoFar + Leg,
    travel(Next, Goal, [Next | Visited], Path, NewDistance, Total).

shortest_route(Start, Goal, Path, Distance) :-
    findall(DistanceValue-(Candidate),
        city_path(Start, Goal, Candidate, DistanceValue),
        Routes),
    keysort(Routes, [Distance-Path | _]).

main :-
    shortest_route(chennai, delhi, Path, Distance),
    format('Shortest route by distance: ~w~nDistance: ~w km~n', [Path, Distance]).

% Query: ?- shortest_route(chennai, delhi, Path, Distance).