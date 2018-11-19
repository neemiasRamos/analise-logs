# Análise de Logs
Projeto do Nanodegree em Desenvolvimento web full-stack da Udacity.
O desafiso é desenvolver um algoritmo python para mostrar relatórios a partir de uma base de dados.

### Criar Views
Este projeto utiliza de views, criadas no banco de dados e referenciadas no `analise_log.py`, para o algoritmo funcionar corretamente, as views devem ser criadas no banco de dados `news`.

1) Para criar a view `view_artigos_populares`:
```sql
create view view_artigos_populares as
select articles.title, count(log.path) as views
from log, articles
where log.status = '200 OK' and log.path like concat('%', articles.slug)
group by log.path, articles.title
order by views desc limit 3;
```

2) Para criar a view `view_autores_populares`:
```sql
create view view_autores_populares as
select authors.name, count(articles.author) as views
from log, articles, authors
where log.status = '200 OK' and log.path like concat('%', articles.slug) and articles.author=authors.id
group by articles.author, authors.name
order by views desc;
```

3) Para criar a view `view_porcentagem_erros`:
```sql
create view view_porcentagem_erros as
select * from
(select to_char(ers.data, 'Mon DD, YYYY') as data, ers.erros::decimal / oks.validos * 100 as porcentagem from
(select date(log.time) as data, count(date(log.time)) as erros
from log
where log.status != '200 OK'
group by date(log.time)
order by erros desc ) as ers,
(select date(log.time) as data, count(date(log.time)) as validos
from log where log.status = '200 OK'
group by date(log.time)
order by validos desc ) as oks
where ers.data = oks.data
order by porcentagem desc) as consulta
where porcentagem > 1;
```


### Instalar e Executar
* Python 3.5
* Este repositório contém arquivos que devem ser inseridos na pasta compartilhada do vagrant;
* É necessário instalar uma VM com as configurações ja definidas, acesse esse [link](https://classroom.udacity.com/nanodegrees/nd004-br/parts/302d2209-30c1-4b9e-8615-2a1f4a5ee7c6/modules/e4147fc0-3658-48bf-8a6c-542fa272d0cd/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) e siga as instruções para instalar a VM;
* Em seguinda efetue o download da [base de dados](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip);
* Com a VM em pleno funcionamento, acesse o diretorio compartilhado e execute o comando  `psql -d news -f newsdata.sql`;
* Clone ou baixe o repositório no diretório compartilhado, vagrant;
* No terminal da máquina virtual, execute `python analise_log.py`.

