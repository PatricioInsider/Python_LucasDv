% --------------------------------------------------
% ---            BASE DE CONOCIMIENTO            ---
% ---              Familia Ficticia              ---
% --------------------------------------------------

% ---------- HECHOS ----------
% Estos son los datos base, las verdades absolutas de nuestro mundo.

% Hechos de Género (predicado con aridad 1)
hombre(pedro).
hombre(juan).
hombre(pablo).
hombre(luis).

mujer(ana).
mujer(maria).
mujer(sofia).

% Hechos de Progenitores (predicado con aridad 2)
% Pedro y Ana son los abuelos
padre_de(pedro, juan).
madre_de(ana, juan).
padre_de(pedro, pablo).
madre_de(ana, pablo).

% Juan y Maria son padres de Luis y Sofia
padre_de(juan, luis).
madre_de(maria, luis).
padre_de(juan, sofia).
madre_de(maria, sofia).


% ---------- REGLAS ----------
% Estas son las reglas que nos permiten inferir conocimiento nuevo.

% Regla: Un progenitor es un padre O una madre.
progenitor_de(X, Y) :- padre_de(X, Y).
progenitor_de(X, Y) :- madre_de(X, Y).

% Reglas: Definen hijo e hija usando el género.
hijo_de(Hijo, Progenitor) :- 
    progenitor_de(Progenitor, Hijo),
    hombre(Hijo).

hija_de(Hija, Progenitor) :-
    progenitor_de(Progenitor, Hija),
    mujer(Hija).

% Reglas: Definen abuelo y abuela.
abuelo_de(Abuelo, Nieto) :-
    progenitor_de(Abuelo, Padre),
    progenitor_de(Padre, Nieto),
    hombre(Abuelo).

abuela_de(Abuela, Nieto) :-
    progenitor_de(Abuela, Madre),
    progenitor_de(Madre, Nieto),
    mujer(Abuela).

% Reglas: Definen hermano y hermana.
% Dos personas son hermanos si comparten un progenitor y no son la misma persona.
hermano_de(Hermano, Persona) :-
    progenitor_de(Progenitor, Hermano),
    progenitor_de(Progenitor, Persona),
    hombre(Hermano),
    Hermano \= Persona. % El operador \= significa "no es igual a"

hermana_de(Hermana, Persona) :-
    progenitor_de(Progenitor, Hermana),
    progenitor_de(Progenitor, Persona),
    mujer(Hermana),
    Hermana \= Persona.

% Regla: Definen la relación de tío.
% T es tío de S si T es hermano de P, y P es progenitor de S.
tio_de(Tio, Sobrino) :-
    hermano_de(Tio, Progenitor),
    progenitor_de(Progenitor, Sobrino).