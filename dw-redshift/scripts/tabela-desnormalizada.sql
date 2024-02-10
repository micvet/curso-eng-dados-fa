SELECT cliente, data, nome as vendedor, produto, quantidade, total
INTO fatovendas --cria uma nova tabela chamada fatovendas com base na consulta
FROM vendas v
INNER JOIN clientes c on (c.idcliente = v.idcliente)
INNER JOIN itensvenda i on (i.idvenda = v.idvenda)
INNER JOIN produtos p on (p.idproduto = i.idproduto)
INNER JOIN vendedores vn on (vn.idvendedor = v.idvendedor)
