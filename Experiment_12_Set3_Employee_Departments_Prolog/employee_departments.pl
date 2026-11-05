department(alice, engineering).
department(bob, engineering).
department(carol, sales).
department(david, sales).
manager(alice, engineering).
manager(carol, sales).
reports_to(bob, alice).
reports_to(david, carol).

employee_department(Employee, Department) :- department(Employee, Department).
department_manager(Department, Manager) :- manager(Manager, Department).
works_under(Employee, Manager) :- reports_to(Employee, Manager).
works_under(Employee, Manager) :-
    reports_to(Employee, Supervisor),
    works_under(Supervisor, Manager).

main :-
    findall(Employee, works_under(Employee, alice), Team),
    format('Employees working under alice: ~w~n', [Team]),
    department_manager(sales, Manager),
    format('Manager of sales: ~w~n', [Manager]).

% Queries: ?- employee_department(bob, Department).
%          ?- works_under(Employee, alice).