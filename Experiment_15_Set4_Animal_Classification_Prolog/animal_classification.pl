has_trait(dog, hair).
has_trait(dog, gives_birth).
has_trait(eagle, feathers).
has_trait(eagle, lays_eggs).
has_trait(snake, scales).
has_trait(snake, cold_blooded).
has_trait(dolphin, lives_in_water).
has_trait(dolphin, breathes_air).
has_trait(shark, lives_in_water).
has_trait(shark, breathes_with_gills).

animal_class(dog, mammal) :- has_trait(dog, hair), has_trait(dog, gives_birth).
animal_class(eagle, bird) :- has_trait(eagle, feathers), has_trait(eagle, lays_eggs).
animal_class(snake, reptile) :- has_trait(snake, scales), has_trait(snake, cold_blooded).
animal_class(Animal, aquatic_animal) :- has_trait(Animal, lives_in_water).

main :-
    forall(animal_class(Animal, Class), format('~w is a ~w.~n', [Animal, Class])).

% Query: ?- animal_class(Animal, Class).