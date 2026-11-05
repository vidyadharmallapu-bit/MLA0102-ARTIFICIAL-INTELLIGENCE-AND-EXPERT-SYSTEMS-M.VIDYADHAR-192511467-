symptom(fever).
symptom(cough).
symptom(headache).
symptom(cold).

possible_disease(flu) :- symptom(fever), symptom(cough), symptom(headache).
possible_disease(common_cold) :- symptom(cough), symptom(cold).
possible_disease(migraine) :- symptom(headache), \+ symptom(fever).

main :-
    findall(Disease, possible_disease(Disease), Diseases),
    format('Possible diseases for the supplied symptoms: ~w~n', [Diseases]).

% This is an educational example, not a medical diagnostic tool.
% Change symptom/1 facts to test other combinations.