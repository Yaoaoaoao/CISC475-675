-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2017-03-04 22:47:35.37

-- tables

-- Table: questionnaire
CREATE TABLE questionnaire (
    id integer NOT NULL CONSTRAINT questionnaire_pk PRIMARY KEY,
    title text NOT NULL,
    description text NOT NULL
);

-- Table: question
CREATE TABLE question (
    id integer NOT NULL CONSTRAINT question_pk PRIMARY KEY,
    questionnaire_id integer NOT NULL,
    question_order integer NOT NULL,
    question_text text NOT NULL,
    question_type varchar(25) NOT NULL,
    CONSTRAINT question_questionnaire FOREIGN KEY (questionnaire_id)
    REFERENCES questionnaire (id)
);

-- Table: option
CREATE TABLE option (
    id integer NOT NULL CONSTRAINT option_pk PRIMARY KEY,
    question_id integer NOT NULL,
    option_order integer NOT NULL,
    option_text text NOT NULL,
    score integer NOT NULL,
    CONSTRAINT option_question FOREIGN KEY (question_id)
    REFERENCES question (id)
);

-- Table: answer
CREATE TABLE answer (
    id integer NOT NULL CONSTRAINT answer_pk PRIMARY KEY,
    question_id integer NOT NULL,
    patient_id integer NOT NULL,
    submit_date date NOT NULL,
    response text NOT NULL,
    note text NOT NULL,
    CONSTRAINT answer_question FOREIGN KEY (question_id)
    REFERENCES question (id)
);

-- End of file.
