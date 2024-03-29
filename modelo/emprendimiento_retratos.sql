PGDMP  '    3                 |            emprendimiento_retratos    16.1    16.1 !    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16403    emprendimiento_retratos    DATABASE     �   CREATE DATABASE emprendimiento_retratos WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
 '   DROP DATABASE emprendimiento_retratos;
                postgres    false            �            1259    16404    cliente    TABLE     3  CREATE TABLE public.cliente (
    id_cliente integer NOT NULL,
    nombre_cliente character varying NOT NULL,
    apellido_cliente character varying NOT NULL,
    dni_cliente character varying NOT NULL,
    email_cliente character varying NOT NULL,
    fecha_registro_cliente date DEFAULT now() NOT NULL
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            �            1259    16410    cliente_id_cliente_seq    SEQUENCE     �   CREATE SEQUENCE public.cliente_id_cliente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.cliente_id_cliente_seq;
       public          postgres    false    215            �           0    0    cliente_id_cliente_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.cliente_id_cliente_seq OWNED BY public.cliente.id_cliente;
          public          postgres    false    216            �            1259    16411    configuracion    TABLE     �   CREATE TABLE public.configuracion (
    id_config integer NOT NULL,
    titulo_config character varying NOT NULL,
    detalle_config character varying NOT NULL,
    valor_config integer NOT NULL
);
 !   DROP TABLE public.configuracion;
       public         heap    postgres    false            �            1259    16416    configuracion_id_config_seq    SEQUENCE     �   CREATE SEQUENCE public.configuracion_id_config_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.configuracion_id_config_seq;
       public          postgres    false    217            �           0    0    configuracion_id_config_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.configuracion_id_config_seq OWNED BY public.configuracion.id_config;
          public          postgres    false    218            �            1259    16417    pedido    TABLE     �  CREATE TABLE public.pedido (
    id_pedido integer NOT NULL,
    id_cliente integer NOT NULL,
    horas_estimadas character varying NOT NULL,
    horas_reales character varying,
    estado_pedido character varying NOT NULL,
    fecha_presupuestado date NOT NULL,
    fecha_aprobado date,
    fecha_finalizado date,
    fecha_entregado date,
    ruta_referencia character varying NOT NULL,
    id_pedido_visible character varying NOT NULL,
    requisitos_cliente character varying NOT NULL
);
    DROP TABLE public.pedido;
       public         heap    postgres    false            �            1259    16422    pedido_id_pedido_seq    SEQUENCE     �   CREATE SEQUENCE public.pedido_id_pedido_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.pedido_id_pedido_seq;
       public          postgres    false    219            �           0    0    pedido_id_pedido_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.pedido_id_pedido_seq OWNED BY public.pedido.id_pedido;
          public          postgres    false    220            �            1259    16423    recurso    TABLE     $  CREATE TABLE public.recurso (
    id_recurso integer NOT NULL,
    nombre_recurso character varying NOT NULL,
    costo_unitario_recurso money NOT NULL,
    usos_costo_recurso integer NOT NULL,
    categoria_recurso character varying NOT NULL,
    marca_recurso character varying NOT NULL
);
    DROP TABLE public.recurso;
       public         heap    postgres    false            �            1259    16428    recurso_id_recurso_seq    SEQUENCE     �   CREATE SEQUENCE public.recurso_id_recurso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.recurso_id_recurso_seq;
       public          postgres    false    221            �           0    0    recurso_id_recurso_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.recurso_id_recurso_seq OWNED BY public.recurso.id_recurso;
          public          postgres    false    222            )           2604    16429    cliente id_cliente    DEFAULT     x   ALTER TABLE ONLY public.cliente ALTER COLUMN id_cliente SET DEFAULT nextval('public.cliente_id_cliente_seq'::regclass);
 A   ALTER TABLE public.cliente ALTER COLUMN id_cliente DROP DEFAULT;
       public          postgres    false    216    215            +           2604    16430    configuracion id_config    DEFAULT     �   ALTER TABLE ONLY public.configuracion ALTER COLUMN id_config SET DEFAULT nextval('public.configuracion_id_config_seq'::regclass);
 F   ALTER TABLE public.configuracion ALTER COLUMN id_config DROP DEFAULT;
       public          postgres    false    218    217            ,           2604    16431    pedido id_pedido    DEFAULT     t   ALTER TABLE ONLY public.pedido ALTER COLUMN id_pedido SET DEFAULT nextval('public.pedido_id_pedido_seq'::regclass);
 ?   ALTER TABLE public.pedido ALTER COLUMN id_pedido DROP DEFAULT;
       public          postgres    false    220    219            -           2604    16432    recurso id_recurso    DEFAULT     x   ALTER TABLE ONLY public.recurso ALTER COLUMN id_recurso SET DEFAULT nextval('public.recurso_id_recurso_seq'::regclass);
 A   ALTER TABLE public.recurso ALTER COLUMN id_recurso DROP DEFAULT;
       public          postgres    false    222    221            �          0    16404    cliente 
   TABLE DATA           �   COPY public.cliente (id_cliente, nombre_cliente, apellido_cliente, dni_cliente, email_cliente, fecha_registro_cliente) FROM stdin;
    public          postgres    false    215   �'       �          0    16411    configuracion 
   TABLE DATA           _   COPY public.configuracion (id_config, titulo_config, detalle_config, valor_config) FROM stdin;
    public          postgres    false    217   (       �          0    16417    pedido 
   TABLE DATA           �   COPY public.pedido (id_pedido, id_cliente, horas_estimadas, horas_reales, estado_pedido, fecha_presupuestado, fecha_aprobado, fecha_finalizado, fecha_entregado, ruta_referencia, id_pedido_visible, requisitos_cliente) FROM stdin;
    public          postgres    false    219   +(       �          0    16423    recurso 
   TABLE DATA           �   COPY public.recurso (id_recurso, nombre_recurso, costo_unitario_recurso, usos_costo_recurso, categoria_recurso, marca_recurso) FROM stdin;
    public          postgres    false    221   H(       �           0    0    cliente_id_cliente_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.cliente_id_cliente_seq', 1, true);
          public          postgres    false    216            �           0    0    configuracion_id_config_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.configuracion_id_config_seq', 1, false);
          public          postgres    false    218            �           0    0    pedido_id_pedido_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.pedido_id_pedido_seq', 1, false);
          public          postgres    false    220            �           0    0    recurso_id_recurso_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.recurso_id_recurso_seq', 1, false);
          public          postgres    false    222            /           2606    16434    cliente cliente_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente);
 >   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pkey;
       public            postgres    false    215            1           2606    16436     configuracion configuracion_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.configuracion
    ADD CONSTRAINT configuracion_pkey PRIMARY KEY (id_config);
 J   ALTER TABLE ONLY public.configuracion DROP CONSTRAINT configuracion_pkey;
       public            postgres    false    217            3           2606    16438 	   pedido id 
   CONSTRAINT     N   ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT id PRIMARY KEY (id_pedido);
 3   ALTER TABLE ONLY public.pedido DROP CONSTRAINT id;
       public            postgres    false    219            5           2606    16440    recurso recurso_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.recurso
    ADD CONSTRAINT recurso_pkey PRIMARY KEY (id_recurso);
 >   ALTER TABLE ONLY public.recurso DROP CONSTRAINT recurso_pkey;
       public            postgres    false    221            6           2606    16441    pedido cliente    FK CONSTRAINT     z   ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT cliente FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente);
 8   ALTER TABLE ONLY public.pedido DROP CONSTRAINT cliente;
       public          postgres    false    215    219    4655            �   B   x�3�tq�t�vu��4167�4�0�L)N,M�76sH�M���K���4202�50�5������ �}#      �      x������ � �      �      x������ � �      �      x������ � �     