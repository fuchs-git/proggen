CREATE TABLE witcher_characters (
    id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name                TEXT NOT NULL,
    species             TEXT,
    gender              TEXT,
    age_group           TEXT,
    origin_or_region    TEXT,
    affiliation         TEXT,
    role_or_occupation  TEXT,
    notable_traits      TEXT,
    abilities_or_skills TEXT,
    first_appearance    TEXT,

    strength            INTEGER CHECK (strength BETWEEN 0 AND 100),
    health              INTEGER CHECK (health BETWEEN 0 AND 100),
    mana                INTEGER CHECK (mana BETWEEN 0 AND 100),
    level               INTEGER CHECK (level BETWEEN 0 AND 100)
);
