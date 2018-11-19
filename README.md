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
Clone ou baixe o repositório no diretório compartilhado, Vagrant.
No terminal da máquina virtual, execute `python analise_log.py`.
