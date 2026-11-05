book('Artificial Intelligence', 'Stuart Russell', available).
book('Prolog Programming', 'Ivan Bratko', checked_out).
book('Algorithms', 'Thomas Cormen', available).

author_of_book(Title, Author) :- book(Title, Author, _).
book_is_available(Title) :- book(Title, _, available).

main :-
    author_of_book('Artificial Intelligence', Author),
    format('Author of Artificial Intelligence: ~w~n', [Author]),
    (book_is_available('Artificial Intelligence')
        -> writeln('Artificial Intelligence is available.')
        ;  writeln('Artificial Intelligence is not available.')),
    (book_is_available('Prolog Programming')
        -> writeln('Prolog Programming is available.')
        ;  writeln('Prolog Programming is not available.')).

% Queries: ?- author_of_book(Title, Author).
%          ?- book_is_available('Algorithms').