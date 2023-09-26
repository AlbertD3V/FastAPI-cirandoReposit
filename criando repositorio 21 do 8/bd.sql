PRAGMA foreign_keys=ON;

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS cardarpio (
    codigo TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL
);

INSERT OR IGNORE INTO cardarpio (codigo,nome,descricao)
VALUES 
    ('massa','Massa','Massas seletivas'),
    ('sobremesa','Sobremesa','Sobremesa especial'),
    ('fastfood','Fasfood','Pao,carne,ovos,galinha e calabresa');


CREATE TABLE IF NOT EXISTS produto (
    codigo TEXT PRIMARY KEY,
    codigo_cardapio TEXT NOT NULL,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    restricao TEXT NOT NULL,
    FOREIGN KEY(codigo_cardapio) REFERENCES cardapio(codigo)
    ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- INSERT OR IGNORE INTO produto (codigo,codigo_cardapio,nome,descricao,preco,restricao)
-- VALUES
--     ('parafuso','massa','MacParafuso','Macarrao soltinho',27.33,'normal'),
--     ('pudim','sobremesa','Pudim cremoso','Leite condensado e ovos',19.45,'normal'),
--     ('hamburguer','fastfood','X-Tudo','Pao\,carne\,ovos\,galinha e calabresa',47.55,'normal');

-- INSERT OR IGNORE INTO produto (nome, descricao, preco, restricao, codigo_cardapio, codigo)
-- VALUES
--     ('Penne', 'Penne ao molho', 19.90, 'vegetariano', 'massa', 'penne'),
--     ('Talharim', 'Talharim ao molho', 19.90, 'vegetariano', 'massa', 'talharim'),
--     ('Petit Gateau', 'Petit Gateau', 9.90, 'vegetariano', 'sobremesa', 'petit-gateau'),
--     ('Batata Frita', 'Batata Frita', 10.90, 'vegano', 'fastfood', 'batata-frita'),
--     ('X Burguer', 'Hambúrguer com Queijo', 15.90, 'padrao', 'fastfood', 'x-burguer');

COMMIT;

