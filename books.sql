--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5 (Postgres.app)
-- Dumped by pg_dump version 17.5 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    id integer NOT NULL,
    title text,
    author text,
    published_date date
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.books_id_seq OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books (id, title, author, published_date) FROM stdin;
1	1984	George Orwell	1949-01-01
2	To Kill a Mockingbird	Harper Lee	1960-01-01
3	The Great Gatsby	F. Scott Fitzgerald	1925-01-01
4	Brave New World	Aldous Huxley	1932-01-01
5	Catch-22	Joseph Heller	1961-01-01
6	The Catcher in the Rye	J.D. Salinger	1951-01-01
7	Fahrenheit 451	Ray Bradbury	1953-01-01
8	Animal Farm	George Orwell	1945-01-01
9	Lord of the Flies	William Golding	1954-01-01
10	Of Mice and Men	John Steinbeck	1937-01-01
11	Slaughterhouse-Five	Kurt Vonnegut	1969-01-01
12	One Hundred Years of Solitude	Gabriel Garcia Marquez	1967-01-01
13	The Hobbit	J.R.R. Tolkien	1937-01-01
14	The Stranger	Albert Camus	1942-01-01
15	Crime and Punishment	Fyodor Dostoevsky	1866-01-01
16	Jane Eyre	Charlotte Brontë	1847-01-01
17	The Brothers Karamazov	Fyodor Dostoevsky	1880-01-01
18	Wuthering Heights	Emily Brontë	1847-01-01
19	The Picture of Dorian Gray	Oscar Wilde	1890-01-01
20	A Tale of Two Cities	Charles Dickens	1859-01-01
\.


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.books_id_seq', 3, true);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

