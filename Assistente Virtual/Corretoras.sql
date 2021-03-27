create table Corretora (
Cod_Corretora int primary key not null,
nome_corretora varchar (40) not null,
Experiencia_investidor varchar (40) not null,
segurança varchar(40) not null,
avaliação_final varchar (40) not null,
Custos_mensais_3op real not null,
Custos_mensais_5op real not null,
Custos_mensais_10op real not null);

insert into Corretora values
(3 , 'XpXP INVESTIMENTOS CCTVM S/A', '5 estrelas', '5 estrelas', '91%', 56.70, 94.50, 189.00),
(147 , 'ATIVA INVESTIMENTOS S.A. CTCV', '4 estrelas', '5 estrelas', '86%', 45.00, 75.00, 150.00),
(386 , 'RICO INVESTIMENTOS', '4 estrelas', '5 estrelas', '86%', 26.70, 44.50, 89.00),
(72 , 'BRADESCO S/A CTVM', '4 estrelas', '5 estrelas', '85%', 44.99, 62.50, 250.00),
(735 , 'ICAP DO BRASIL CTVM LTDA', '4 estrelas', '5 estrelas', '81%', 30.00, 50.00, 100.00),
(114 , 'ITAU CV S/A', '4 estrelas', '5 estrelas', '79%', 48.00, 125.00, 400.00),
(90 , 'EASYNVEST – TITULO CV S.A.', '4 estrelas', '5 estrelas', '75%', 30.00, 50.00, 100.00),
(262 , 'MIRAE ASSET WEALTH MANAGEMENT', '3 estrelas', '5 estrelas', '64%', 13.75, 15.73, 20.68),
(820 , 'BB BANCO DE INVESTIMENTO S/A', '3 estrelas', ' 5 estrelas', '60%', 60.78, 103.25, 213.00),
(27 , 'SANTANDER CCVM S/A', '3 estrelas', '5 estrelas', '60%', 45.00, 112.50, 350.00);

select * from Corretora;
