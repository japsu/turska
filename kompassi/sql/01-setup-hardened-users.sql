BEGIN;
ALTER USER kompassi NOSUPERUSER;
CREATE USER kompassi_ddl NOSUPERUSER;
ALTER DATABASE kompassi OWNER TO kompassi_ddl;
REASSIGN OWNED BY kompassi TO kompassi_ddl;
COMMIT;
