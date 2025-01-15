-- Luodaan person-taulu ja sen sarakkeet
CREATE TABLE public.person2
(
    idnumero SERIAL PRIMARY KEY,
    etunimi CHARACTER VARYING NOT NULL,
    sukunimi CHARACTER VARYING NOT NULL
);