--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: patient_diagnostic; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE patient_diagnostic (
    id integer NOT NULL,
    code character varying(64) NOT NULL,
    name text NOT NULL,
    tipo text NOT NULL
);


ALTER TABLE public.patient_diagnostic OWNER TO postgres;

--
-- Name: patient_diagnostic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE patient_diagnostic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_diagnostic_id_seq OWNER TO postgres;

--
-- Name: patient_diagnostic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE patient_diagnostic_id_seq OWNED BY patient_diagnostic.id;


--
-- Name: patient_entity; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE patient_entity (
    id integer NOT NULL,
    name character varying(64) NOT NULL
);


ALTER TABLE public.patient_entity OWNER TO postgres;

--
-- Name: patient_entity_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE patient_entity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_entity_id_seq OWNER TO postgres;

--
-- Name: patient_entity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE patient_entity_id_seq OWNED BY patient_entity.id;


--
-- Name: patient_patient; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE patient_patient (
    id integer NOT NULL,
    id_type character varying(64) NOT NULL,
    id_num character varying(64) NOT NULL,
    name character varying(64) NOT NULL,
    lastname character varying(64) NOT NULL,
    genre character varying(64) NOT NULL,
    occupation character varying(64) NOT NULL,
    birthday date NOT NULL,
    is_active boolean NOT NULL,
    entity_id integer NOT NULL
);


ALTER TABLE public.patient_patient OWNER TO postgres;

--
-- Name: patient_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE patient_patient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_patient_id_seq OWNER TO postgres;

--
-- Name: patient_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE patient_patient_id_seq OWNED BY patient_patient.id;


--
-- Name: patient_patient_list_diagnostic; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE patient_patient_list_diagnostic (
    id integer NOT NULL,
    patient_id integer NOT NULL,
    diagnostic_id integer NOT NULL
);


ALTER TABLE public.patient_patient_list_diagnostic OWNER TO postgres;

--
-- Name: patient_patient_list_diagnostic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE patient_patient_list_diagnostic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_patient_list_diagnostic_id_seq OWNER TO postgres;

--
-- Name: patient_patient_list_diagnostic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE patient_patient_list_diagnostic_id_seq OWNED BY patient_patient_list_diagnostic.id;


--
-- Name: start_gamesession; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_gamesession (
    id integer NOT NULL,
    date date NOT NULL,
    score integer NOT NULL,
    repetitions integer NOT NULL,
    "time" integer NOT NULL,
    level integer NOT NULL,
    minigame_id integer NOT NULL,
    therapy_id integer NOT NULL
);


ALTER TABLE public.start_gamesession OWNER TO postgres;

--
-- Name: start_gamesession_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_gamesession_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_gamesession_id_seq OWNER TO postgres;

--
-- Name: start_gamesession_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_gamesession_id_seq OWNED BY start_gamesession.id;


--
-- Name: start_minigame; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_minigame (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    description character varying(1024) NOT NULL
);


ALTER TABLE public.start_minigame OWNER TO postgres;

--
-- Name: start_minigame_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_minigame_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_minigame_id_seq OWNER TO postgres;

--
-- Name: start_minigame_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_minigame_id_seq OWNED BY start_minigame.id;


--
-- Name: start_minigame_movements; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_minigame_movements (
    id integer NOT NULL,
    minigame_id integer NOT NULL,
    movement_id integer NOT NULL
);


ALTER TABLE public.start_minigame_movements OWNER TO postgres;

--
-- Name: start_minigame_movements_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_minigame_movements_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_minigame_movements_id_seq OWNER TO postgres;

--
-- Name: start_minigame_movements_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_minigame_movements_id_seq OWNED BY start_minigame_movements.id;


--
-- Name: start_movement; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_movement (
    id integer NOT NULL,
    name character varying(64) NOT NULL
);


ALTER TABLE public.start_movement OWNER TO postgres;

--
-- Name: start_movement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_movement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_movement_id_seq OWNER TO postgres;

--
-- Name: start_movement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_movement_id_seq OWNED BY start_movement.id;


--
-- Name: start_performance; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_performance (
    id integer NOT NULL,
    angle integer NOT NULL,
    game_session_id integer NOT NULL,
    movement_id integer NOT NULL
);


ALTER TABLE public.start_performance OWNER TO postgres;

--
-- Name: start_performance_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_performance_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_performance_id_seq OWNER TO postgres;

--
-- Name: start_performance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_performance_id_seq OWNED BY start_performance.id;


--
-- Name: start_therapysession; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE start_therapysession (
    id integer NOT NULL,
    date date NOT NULL,
    objective character varying(128) NOT NULL,
    description character varying(1024) NOT NULL,
    patient_id integer NOT NULL,
    therapist_id integer NOT NULL
);


ALTER TABLE public.start_therapysession OWNER TO postgres;

--
-- Name: start_therapysession_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE start_therapysession_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.start_therapysession_id_seq OWNER TO postgres;

--
-- Name: start_therapysession_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE start_therapysession_id_seq OWNED BY start_therapysession.id;


--
-- Name: therapist_therapist; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE therapist_therapist (
    user_ptr_id integer NOT NULL,
    name character varying(64) NOT NULL,
    lastname character varying(64) NOT NULL,
    id_type character varying(64) NOT NULL,
    genre character varying(64) NOT NULL
);


ALTER TABLE public.therapist_therapist OWNER TO postgres;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_diagnostic ALTER COLUMN id SET DEFAULT nextval('patient_diagnostic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_entity ALTER COLUMN id SET DEFAULT nextval('patient_entity_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_patient ALTER COLUMN id SET DEFAULT nextval('patient_patient_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_patient_list_diagnostic ALTER COLUMN id SET DEFAULT nextval('patient_patient_list_diagnostic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_gamesession ALTER COLUMN id SET DEFAULT nextval('start_gamesession_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_minigame ALTER COLUMN id SET DEFAULT nextval('start_minigame_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_minigame_movements ALTER COLUMN id SET DEFAULT nextval('start_minigame_movements_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_movement ALTER COLUMN id SET DEFAULT nextval('start_movement_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_performance ALTER COLUMN id SET DEFAULT nextval('start_performance_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_therapysession ALTER COLUMN id SET DEFAULT nextval('start_therapysession_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add therapy session	7	add_therapysession
20	Can change therapy session	7	change_therapysession
21	Can delete therapy session	7	delete_therapysession
22	Can add movement	8	add_movement
23	Can change movement	8	change_movement
24	Can delete movement	8	delete_movement
25	Can add minigame	9	add_minigame
26	Can change minigame	9	change_minigame
27	Can delete minigame	9	delete_minigame
28	Can add game session	10	add_gamesession
29	Can change game session	10	change_gamesession
30	Can delete game session	10	delete_gamesession
31	Can add performance	11	add_performance
32	Can change performance	11	change_performance
33	Can delete performance	11	delete_performance
34	Can add entity	12	add_entity
35	Can change entity	12	change_entity
36	Can delete entity	12	delete_entity
37	Can add diagnostic	13	add_diagnostic
38	Can change diagnostic	13	change_diagnostic
39	Can delete diagnostic	13	delete_diagnostic
43	Can add user	15	add_therapist
44	Can change user	15	change_therapist
45	Can delete user	15	delete_therapist
46	Can add patient	16	add_patient
47	Can change patient	16	change_patient
48	Can delete patient	16	delete_patient
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 48, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
8	pbkdf2_sha256$24000$mfvfiIfvNyxP$B5G5tsTI77NBgBOnM9dCEu+VH+IFql4JLXtxhMl1Jt0=	\N	f	54321				f	f	2016-10-31 14:38:43.595001+00
9	pbkdf2_sha256$24000$QEIizyNcTHm3$DoHD1xGD9aT9v6IUWSWWBoKQ27/mwu0ZdjUjqlqaMKw=	\N	f	111234546				f	t	2016-11-08 15:48:43.173622+00
1	pbkdf2_sha256$24000$5gckqr1LsZN0$HQwO2GC+j966/+Em+Vn2QVTOu34KnMq0dqt15pwE00g=	2016-11-08 20:34:13.498859+00	t	admin				t	t	2016-10-23 00:33:11.001012+00
3	123	\N	f	1144067370				f	f	2016-10-23 01:19:21.763346+00
6	123	\N	f	1144067				f	t	2016-10-23 20:21:24.225874+00
7	pbkdf2_sha256$24000$arsl4pnUzMJf$BcGwVKYYxqyD0pVpSc2iVtdvfDh9dVqIlR5vBNaucaA=	2016-10-25 21:44:45.779819+00	f	987654321				f	t	2016-10-25 21:32:56.881368+00
2	123	\N	f	123123123123				f	f	2016-10-23 01:17:21.521935+00
4	pbkdf2_sha256$24000$kUNxlRL56JDS$gopCGhJk4QmzswDbmQio7XINoLByjGkBPAJX1lQdAEo=	\N	f	000000				f	t	2016-10-23 20:18:54.058299+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 9, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2016-10-23 00:58:53.582419+00	1	Comfandi	1	Added.	12	1
2	2016-10-25 00:19:46.277259+00	1	Diagnostic object	1	Added.	13	1
3	2016-10-25 00:20:03.699176+00	2	Diagnostic object	1	Added.	13	1
4	2016-10-25 00:20:40.684819+00	3	Diagnostic object	1	Added.	13	1
5	2016-10-25 00:20:56.938448+00	4	Diagnostic object	1	Added.	13	1
22	2016-11-01 18:04:30.418219+00	5	asdasd	3		15	1
6	2016-10-25 01:17:37.261758+00	22222	Patient object	2	Changed list_diagnostic.	\N	1
7	2016-10-25 01:22:11.105222+00	1345613	1345613 - Monica	2	Changed list_diagnostic.	\N	1
8	2016-10-25 01:22:16.363456+00	1345613	1345613 - Monica	2	No fields changed.	\N	1
9	2016-10-25 01:22:47.258425+00	13123123123	13123123123 - Pepito	2	Changed list_diagnostic.	\N	1
10	2016-10-25 01:40:55.158142+00	sadsdfsgd	sadsdfsgd - asdasdasdad	3		\N	1
11	2016-10-25 01:40:55.260546+00	asd	asd - asdasd	3		\N	1
12	2016-10-25 01:40:55.264791+00	313232323123	313232323123 - asdasd	3		\N	1
13	2016-10-25 01:40:55.269984+00	3123231	3123231 - asdasd	3		\N	1
14	2016-10-25 01:40:55.27632+00	22222	22222 - asdasdasdad	3		\N	1
15	2016-10-25 01:40:55.279809+00	131231312	131231312 - asdasda	3		\N	1
16	2016-10-25 01:40:55.283466+00	13123123	13123123 - asdasda	3		\N	1
17	2016-10-25 01:40:55.2867+00	12312313	12312313 - fsfdf	3		\N	1
18	2016-10-25 01:40:55.288579+00	1231231231321313	1231231231321313 - asdasdasdad	3		\N	1
19	2016-10-25 01:40:55.291786+00	123123123123123	123123123123123 - asdasdasdad	3		\N	1
20	2016-10-25 01:40:55.294925+00	123123	123123 - asdasd	3		\N	1
21	2016-10-25 01:40:55.296856+00	123	123 - asdasd	3		\N	1
23	2016-11-08 20:27:28.468841+00	1	Patada kung Fu	1	Added.	8	1
24	2016-11-08 20:27:30.563009+00	1	Minigame object	1	Added.	9	1
25	2016-11-08 20:29:58.671557+00	1	TherapySession object	1	Added.	7	1
26	2016-11-08 20:32:13.89395+00	1	GameSession object	1	Added.	10	1
27	2016-11-08 21:55:09.281969+00	2	Levantamiento de brazos	1	Added.	8	1
28	2016-11-08 22:00:35.935661+00	3	Flexión de rodilla	1	Added.	8	1
29	2016-11-08 22:03:29.186817+00	4	Flexión de codo	1	Added.	8	1
30	2016-11-08 22:04:29.073907+00	1	Performance object	1	Added.	11	1
31	2016-11-08 22:04:46.049243+00	2	Performance object	1	Added.	11	1
32	2016-11-08 22:05:13.494689+00	3	Performance object	1	Added.	11	1
33	2016-11-08 22:06:58.186789+00	2	Armando - Casimiro	1	Added.	7	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 33, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	start	therapysession
8	start	movement
9	start	minigame
10	start	gamesession
11	start	performance
12	patient	entity
13	patient	diagnostic
15	therapist	therapist
16	patient	patient
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 16, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2016-10-23 00:32:53.628584+00
2	auth	0001_initial	2016-10-23 00:32:53.745524+00
3	admin	0001_initial	2016-10-23 00:32:53.780639+00
4	admin	0002_logentry_remove_auto_add	2016-10-23 00:32:53.797134+00
5	contenttypes	0002_remove_content_type_name	2016-10-23 00:32:53.833207+00
6	auth	0002_alter_permission_name_max_length	2016-10-23 00:32:53.848585+00
7	auth	0003_alter_user_email_max_length	2016-10-23 00:32:53.863722+00
8	auth	0004_alter_user_username_opts	2016-10-23 00:32:53.875634+00
9	auth	0005_alter_user_last_login_null	2016-10-23 00:32:53.891635+00
10	auth	0006_require_contenttypes_0002	2016-10-23 00:32:53.895162+00
11	auth	0007_alter_validators_add_error_messages	2016-10-23 00:32:53.906729+00
12	patient	0001_initial	2016-10-23 00:32:53.976935+00
13	sessions	0001_initial	2016-10-23 00:32:54.004842+00
14	therapist	0001_initial	2016-10-23 00:32:54.035736+00
15	start	0001_initial	2016-10-23 00:32:54.096482+00
16	start	0002_auto_20161023_0030	2016-10-23 00:32:54.216545+00
17	therapist	0002_remove_therapist_id_num	2016-10-23 00:49:58.033179+00
18	patient	0002_auto_20161102_2144	2016-11-02 21:44:59.692033+00
19	therapist	0003_auto_20161102_2144	2016-11-02 21:44:59.813455+00
20	start	0003_auto_20161103_2048	2016-11-03 20:48:14.717673+00
21	patient	0003_auto_20161103_2048	2016-11-03 20:48:14.82128+00
22	patient	0004_patient	2016-11-03 20:50:40.045326+00
23	start	0004_auto_20161103_2050	2016-11-03 20:50:40.333836+00
24	patient	0005_auto_20161103_2119	2016-11-03 21:19:30.901979+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 24, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
g2zlm6ee31lsfu2cfy4pyglxbtgj6tli	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-06 18:14:28.500737+00
lm4il43zfhmwzp32c7agyvmym0gebmfj	MjlhY2JhNzJhZTE0YWE3NzU0ODlhNDhiN2JkNWM3MTliZDU5ZTI4MTp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2016-11-07 00:46:28.213834+00
r223854lxie79s2e7r9p2cbonw5p46d4	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-08 17:19:48.467902+00
t5tdfwmsc6opjvjd3cic7rntx27x8eyk	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-15 16:49:02.370366+00
1nwohpeyxwaa1bxo146y1ddgklo2f3zk	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-15 20:15:01.447482+00
cp4s5nyul1fcbsh8n3vy40f7fqajrytw	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-16 21:36:47.346354+00
p0tlfudn3qe3go7s3mzlpe0bxewy6zlz	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 03:25:22.797162+00
ifweta18hvp0jf1n38vfbsmg6zi7lb5f	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 03:39:06.184225+00
9ylbjy6l8m400snj3ucqv8e2mp1p4ghs	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 19:35:08.320483+00
81uki9t2q5cu06ol1a0nhbpxne5gyy1h	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 19:38:23.058039+00
tq0fy9huftohjl3o6x9tdnjtxmjqy9x3	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 19:46:37.788935+00
2sj3sioqweccs0p8ga0brmj24cykcf4x	ODBkOTE1ZWM0ZTY1MDNlODEwZWQ2MWJjZTZlNmNkMGRjM2NkNzA1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMGE3Y2YzZDE1MDJiNmFkYTcwODgyZmMxMDNiNzM0ZDcxNGE2ZjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2016-11-17 21:08:56.703873+00
\.


--
-- Data for Name: patient_diagnostic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY patient_diagnostic (id, code, name, tipo) FROM stdin;
1	J449	ENFERMEDAD PULMONAR OBSTRUCTIVA CRÓNICA NO ESPECIFICADA.	Rehabilitación Pulmonar.
2	J459	ASMA NO ESPECIFICADA.	Rehabilitación Pulmonar.
3	J189	NEUMONIA NO ESPECIFICADA.	Rehabilitación Pulmonar.
4	B909	SECUELAS DE TUBERCULOSIS.	Rehabilitación Pulmonar.
\.


--
-- Name: patient_diagnostic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('patient_diagnostic_id_seq', 4, true);


--
-- Data for Name: patient_entity; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY patient_entity (id, name) FROM stdin;
1	Comfandi
\.


--
-- Name: patient_entity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('patient_entity_id_seq', 1, true);


--
-- Data for Name: patient_patient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY patient_patient (id, id_type, id_num, name, lastname, genre, occupation, birthday, is_active, entity_id) FROM stdin;
1	Cédula de extranjeria	12345694	Prueba Paciente	Tester modificar	Masculino	Ingeniero	1989-08-09	f	1
2	Cédula de ciudadania	00000	Pepito	Perez	Masculino	Estudiante	2016-11-22	t	1
3	Cédula de ciudadania	00001	Armando	Casas	Masculino	Estudiante	2008-12-29	t	1
\.


--
-- Name: patient_patient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('patient_patient_id_seq', 3, true);


--
-- Data for Name: patient_patient_list_diagnostic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY patient_patient_list_diagnostic (id, patient_id, diagnostic_id) FROM stdin;
1	1	1
2	2	2
3	2	3
4	3	1
5	3	4
\.


--
-- Name: patient_patient_list_diagnostic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('patient_patient_list_diagnostic_id_seq', 5, true);


--
-- Data for Name: start_gamesession; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_gamesession (id, date, score, repetitions, "time", level, minigame_id, therapy_id) FROM stdin;
1	2016-11-02	10	10	1	1	1	1
\.


--
-- Name: start_gamesession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_gamesession_id_seq', 1, true);


--
-- Data for Name: start_minigame; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_minigame (id, name, description) FROM stdin;
1	Samurai chef	Es un samurai chef
\.


--
-- Name: start_minigame_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_minigame_id_seq', 1, true);


--
-- Data for Name: start_minigame_movements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_minigame_movements (id, minigame_id, movement_id) FROM stdin;
1	1	1
\.


--
-- Name: start_minigame_movements_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_minigame_movements_id_seq', 1, true);


--
-- Data for Name: start_movement; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_movement (id, name) FROM stdin;
1	Patada kung Fu
2	Levantamiento de brazos
3	Flexión de rodilla
4	Flexión de codo
\.


--
-- Name: start_movement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_movement_id_seq', 4, true);


--
-- Data for Name: start_performance; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_performance (id, angle, game_session_id, movement_id) FROM stdin;
1	50	1	1
2	90	1	2
3	10	1	3
\.


--
-- Name: start_performance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_performance_id_seq', 3, true);


--
-- Data for Name: start_therapysession; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY start_therapysession (id, date, objective, description, patient_id, therapist_id) FROM stdin;
1	2016-11-02	Aprender una patada kung fu	Pegar patada duro	1	4
2	2016-08-14	Make me feel better	Meka an exercise	3	4
\.


--
-- Name: start_therapysession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('start_therapysession_id_seq', 2, true);


--
-- Data for Name: therapist_therapist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY therapist_therapist (user_ptr_id, name, lastname, id_type, genre) FROM stdin;
3	Armando	Paredes del Castillo	Cédula de ciudadania	Masculino
6	Miguel	Lopez	Cédula de ciudadania	Masculino
7	Camilo	Ruiz Casanova	Cédula de ciudadania	Masculino
2	Pepito	Perez	Cédula de ciudadania	Masculino
4	Casimiro	Tejas	Tarjeta de identidad	Masculino
8	Prueba numero 2	Tester nuevo	Cédula de ciudadania	Femenino
9	prueba	que si	Cédula de ciudadania	Masculino
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: patient_diagnostic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_diagnostic
    ADD CONSTRAINT patient_diagnostic_pkey PRIMARY KEY (id);


--
-- Name: patient_entity_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_entity
    ADD CONSTRAINT patient_entity_pkey PRIMARY KEY (id);


--
-- Name: patient_patient_id_num_e85bf7b8_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_patient
    ADD CONSTRAINT patient_patient_id_num_e85bf7b8_uniq UNIQUE (id_num);


--
-- Name: patient_patient_list_diagnostic_patient_id_5d505b1c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_patient_list_diagnostic
    ADD CONSTRAINT patient_patient_list_diagnostic_patient_id_5d505b1c_uniq UNIQUE (patient_id, diagnostic_id);


--
-- Name: patient_patient_list_diagnostic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_patient_list_diagnostic
    ADD CONSTRAINT patient_patient_list_diagnostic_pkey PRIMARY KEY (id);


--
-- Name: patient_patient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY patient_patient
    ADD CONSTRAINT patient_patient_pkey PRIMARY KEY (id);


--
-- Name: start_gamesession_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_gamesession
    ADD CONSTRAINT start_gamesession_pkey PRIMARY KEY (id);


--
-- Name: start_minigame_movements_minigame_id_91d1c878_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_minigame_movements
    ADD CONSTRAINT start_minigame_movements_minigame_id_91d1c878_uniq UNIQUE (minigame_id, movement_id);


--
-- Name: start_minigame_movements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_minigame_movements
    ADD CONSTRAINT start_minigame_movements_pkey PRIMARY KEY (id);


--
-- Name: start_minigame_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_minigame
    ADD CONSTRAINT start_minigame_pkey PRIMARY KEY (id);


--
-- Name: start_movement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_movement
    ADD CONSTRAINT start_movement_pkey PRIMARY KEY (id);


--
-- Name: start_performance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_performance
    ADD CONSTRAINT start_performance_pkey PRIMARY KEY (id);


--
-- Name: start_therapysession_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY start_therapysession
    ADD CONSTRAINT start_therapysession_pkey PRIMARY KEY (id);


--
-- Name: therapist_therapist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY therapist_therapist
    ADD CONSTRAINT therapist_therapist_pkey PRIMARY KEY (user_ptr_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: patient_patient_dffc4713; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX patient_patient_dffc4713 ON patient_patient USING btree (entity_id);


--
-- Name: patient_patient_list_diagnostic_9f065c57; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX patient_patient_list_diagnostic_9f065c57 ON patient_patient_list_diagnostic USING btree (patient_id);


--
-- Name: patient_patient_list_diagnostic_ac7c5e6b; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX patient_patient_list_diagnostic_ac7c5e6b ON patient_patient_list_diagnostic USING btree (diagnostic_id);


--
-- Name: start_gamesession_0f4fca4e; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_gamesession_0f4fca4e ON start_gamesession USING btree (therapy_id);


--
-- Name: start_gamesession_b43842a6; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_gamesession_b43842a6 ON start_gamesession USING btree (minigame_id);


--
-- Name: start_minigame_movements_b43842a6; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_minigame_movements_b43842a6 ON start_minigame_movements USING btree (minigame_id);


--
-- Name: start_minigame_movements_c0855f58; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_minigame_movements_c0855f58 ON start_minigame_movements USING btree (movement_id);


--
-- Name: start_performance_b8c41820; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_performance_b8c41820 ON start_performance USING btree (game_session_id);


--
-- Name: start_performance_c0855f58; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_performance_c0855f58 ON start_performance USING btree (movement_id);


--
-- Name: start_therapysession_2316e0db; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_therapysession_2316e0db ON start_therapysession USING btree (therapist_id);


--
-- Name: start_therapysession_9f065c57; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX start_therapysession_9f065c57 ON start_therapysession USING btree (patient_id);


--
-- Name: auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: patient_patient_diagnostic_id_91422442_fk_patient_diagnostic_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_patient_list_diagnostic
    ADD CONSTRAINT patient_patient_diagnostic_id_91422442_fk_patient_diagnostic_id FOREIGN KEY (diagnostic_id) REFERENCES patient_diagnostic(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: patient_patient_entity_id_14a15928_fk_patient_entity_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_patient
    ADD CONSTRAINT patient_patient_entity_id_14a15928_fk_patient_entity_id FOREIGN KEY (entity_id) REFERENCES patient_entity(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: patient_patient_list__patient_id_232256ca_fk_patient_patient_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY patient_patient_list_diagnostic
    ADD CONSTRAINT patient_patient_list__patient_id_232256ca_fk_patient_patient_id FOREIGN KEY (patient_id) REFERENCES patient_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start__therapist_id_8d13e3a2_fk_therapist_therapist_user_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_therapysession
    ADD CONSTRAINT start__therapist_id_8d13e3a2_fk_therapist_therapist_user_ptr_id FOREIGN KEY (therapist_id) REFERENCES therapist_therapist(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_gamesessio_therapy_id_ef474d58_fk_start_therapysession_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_gamesession
    ADD CONSTRAINT start_gamesessio_therapy_id_ef474d58_fk_start_therapysession_id FOREIGN KEY (therapy_id) REFERENCES start_therapysession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_gamesession_minigame_id_2b0b13c7_fk_start_minigame_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_gamesession
    ADD CONSTRAINT start_gamesession_minigame_id_2b0b13c7_fk_start_minigame_id FOREIGN KEY (minigame_id) REFERENCES start_minigame(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_minigame_moveme_minigame_id_f40394d4_fk_start_minigame_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_minigame_movements
    ADD CONSTRAINT start_minigame_moveme_minigame_id_f40394d4_fk_start_minigame_id FOREIGN KEY (minigame_id) REFERENCES start_minigame(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_minigame_moveme_movement_id_d47a7ab2_fk_start_movement_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_minigame_movements
    ADD CONSTRAINT start_minigame_moveme_movement_id_d47a7ab2_fk_start_movement_id FOREIGN KEY (movement_id) REFERENCES start_movement(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_performa_game_session_id_207133ca_fk_start_gamesession_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_performance
    ADD CONSTRAINT start_performa_game_session_id_207133ca_fk_start_gamesession_id FOREIGN KEY (game_session_id) REFERENCES start_gamesession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_performance_movement_id_1e4bc066_fk_start_movement_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_performance
    ADD CONSTRAINT start_performance_movement_id_1e4bc066_fk_start_movement_id FOREIGN KEY (movement_id) REFERENCES start_movement(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: start_therapysession_patient_id_9d976815_fk_patient_patient_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY start_therapysession
    ADD CONSTRAINT start_therapysession_patient_id_9d976815_fk_patient_patient_id FOREIGN KEY (patient_id) REFERENCES patient_patient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: therapist_therapist_user_ptr_id_c0a0efb3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY therapist_therapist
    ADD CONSTRAINT therapist_therapist_user_ptr_id_c0a0efb3_fk_auth_user_id FOREIGN KEY (user_ptr_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

