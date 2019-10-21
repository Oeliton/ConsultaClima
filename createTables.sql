CREATE TABLE public.city (
	"name" varchar(100) NOT NULL,
	id serial NOT NULL,
	CONSTRAINT city_pk PRIMARY KEY (id)
);

CREATE TABLE public.history_weather (
	temp_max float4 NULL,
	temp_min float4 NULL,
	date_forecast timestamp NULL,
	date_query timestamp NULL,
	weather varchar NOT NULL,
	id serial NOT NULL,
	id_city int4 NOT NULL,
	CONSTRAINT history_weather_pk PRIMARY KEY (id),
	CONSTRAINT city_fk FOREIGN KEY (id_city) REFERENCES city(id)
);