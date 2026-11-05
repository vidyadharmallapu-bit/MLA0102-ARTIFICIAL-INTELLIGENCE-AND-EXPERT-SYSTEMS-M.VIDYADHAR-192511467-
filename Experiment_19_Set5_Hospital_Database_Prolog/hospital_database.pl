patient('Arun', 34, influenza, 'Dr Rao').
patient('Bina', 52, diabetes, 'Dr Shah').
patient('Chitra', 28, influenza, 'Dr Rao').
patient('Dev', 61, hypertension, 'Dr Iyer').

patients_with_disease(Disease, Names) :-
    findall(Name, patient(Name, _, Disease, _), Names).
patients_treated_by(Doctor, Names) :-
    findall(Name, patient(Name, _, _, Doctor), Names).

main :-
    patients_with_disease(influenza, InfluenzaPatients),
    format('Patients with influenza: ~w~n', [InfluenzaPatients]),
    patients_treated_by('Dr Rao', RaoPatients),
    format('Patients treated by Dr Rao: ~w~n', [RaoPatients]).

% Queries: ?- patients_with_disease(influenza, Patients).
%          ?- patients_treated_by('Dr Rao', Patients).