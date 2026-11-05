weather(cloudy).
weather(windy).
weather(humid).

will_rain :- weather(rainy).
will_rain :- weather(cloudy), weather(humid).
will_not_rain :- weather(sunny), \+ weather(cloudy).

main :-
    (will_rain -> writeln('Prediction: it will rain.')
        ; will_not_rain -> writeln('Prediction: it will not rain.')
        ; writeln('Prediction: insufficient weather facts.')).

% Change weather/1 facts to test different forecast conditions.