father(john, mary).
father(john, peter).
mother(susan, mary).
mother(susan, peter).
father(peter, alice).
mother(linda, alice).
father(peter, ben).
mother(linda, ben).
male(john).
male(peter).
male(ben).
female(susan).
female(linda).
female(mary).
female(alice).

parent(Parent, Child) :- father(Parent, Child).
parent(Parent, Child) :- mother(Parent, Child).
sibling(Person, Other) :-
    parent(Parent, Person), parent(Parent, Other), Person \= Other.
brother(Person, Other) :- sibling(Person, Other), male(Person).
sister(Person, Other) :- sibling(Person, Other), female(Person).
uncle(Person, Child) :- brother(Person, Parent), parent(Parent, Child).
aunt(Person, Child) :- sister(Person, Parent), parent(Parent, Child).
cousin(Person, Other) :-
    parent(Parent, Person), parent(OtherParent, Other),
    sibling(Parent, OtherParent), Person \= Other.

main :-
    findall(Relative, cousin(alice, Relative), Cousins),
    format('Alice\'s cousins: ~w~n', [Cousins]),
    (uncle(john, alice) -> writeln('John is Alice\'s uncle.') ; true).

% Queries: ?- brother(peter, mary).
%          ?- aunt(Aunt, alice).