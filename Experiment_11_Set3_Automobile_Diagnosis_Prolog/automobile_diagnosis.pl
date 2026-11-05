symptom(engine_not_starting).
symptom(battery_low).
symptom(no_fuel).
symptom(flat_tyre).

possible_fault(flat_battery) :- symptom(battery_low).
possible_fault(empty_fuel_tank) :- symptom(no_fuel).
possible_fault(punctured_tyre) :- symptom(flat_tyre).
possible_fault(check_ignition_or_starter) :-
    symptom(engine_not_starting),
    \+ symptom(battery_low),
    \+ symptom(no_fuel).

main :-
    findall(Fault, possible_fault(Fault), Faults),
    format('Possible faults from supplied symptoms: ~w~n', [Faults]).

% Change symptom/1 facts to diagnose a different vehicle.
% Query: ?- possible_fault(Fault).