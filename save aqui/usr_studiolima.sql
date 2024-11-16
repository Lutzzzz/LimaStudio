-- Tabela de Profissionais
CREATE TABLE profissionais (
    id_profissional NUMBER PRIMARY KEY, 
    nome VARCHAR2(255), 
    especialidade VARCHAR2(255),
    numero_atendimentos NUMBER
);

-- Tabela de Clientes
CREATE TABLE clientes (
    id_cliente NUMBER PRIMARY KEY, 
    nome VARCHAR2(255), 
    email VARCHAR2(255), 
    telefone VARCHAR2(50)
);

-- Tabela de Serviços
CREATE TABLE servicos (
    id_servico NUMBER PRIMARY KEY, 
    nome_servico VARCHAR2(255), 
    descricao_servico VARCHAR2(500), 
    preco_servico NUMBER
);

-- Tabela de Agendamentos
CREATE TABLE agendamentos (
    id_agendamento NUMBER PRIMARY KEY,
    id_cliente NUMBER, 
    id_profissional NUMBER, 
    id_servico NUMBER,
    data_hora TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_profissional) REFERENCES profissionais(id_profissional),
    FOREIGN KEY (id_servico) REFERENCES servicos(id_servico)
);

-- Tabela de Estoque
CREATE TABLE estoque (
    id_item NUMBER PRIMARY KEY,
    nome_item VARCHAR2(255),
    quantidade NUMBER,
    descricao VARCHAR2(500),
    data_vencimento DATE,
    preco_unitario NUMBER
);

-- Tabela de Usuários (para login)
CREATE TABLE usuarios (
    id_usuario NUMBER PRIMARY KEY, 
    nome VARCHAR2(255), 
    senha VARCHAR2(255), 
    tipo_usuario VARCHAR2(50)
);

-- Sequências para os IDs
CREATE SEQUENCE seq_profissionais START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_clientes START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_servicos START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_agendamentos START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_estoque START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_usuarios START WITH 1 INCREMENT BY 1;

-- Inserir Profissionais (4 registros)
INSERT INTO profissionais (id_profissional, nome, especialidade, numero_atendimentos) 
VALUES (seq_profissionais.NEXTVAL, 'João Silva', 'Corte de Cabelo', 15);

INSERT INTO profissionais (id_profissional, nome, especialidade, numero_atendimentos) 
VALUES (seq_profissionais.NEXTVAL, 'Maria Oliveira', 'Manicure', 23);

INSERT INTO profissionais (id_profissional, nome, especialidade, numero_atendimentos) 
VALUES (seq_profissionais.NEXTVAL, 'Carlos Souza', 'Pedicure', 12);

INSERT INTO profissionais (id_profissional, nome, especialidade, numero_atendimentos) 
VALUES (seq_profissionais.NEXTVAL, 'Ana Costa', 'Massagem', 8);

-- Inserir Clientes (20 registros)
INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Lucas Pereira', 'lucas.pereira@email.com', '11987654321');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Amanda Silva', 'amanda.silva@email.com', '21987654322');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Pedro Lima', 'pedro.lima@email.com', '31987654323');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Carla Santos', 'carla.santos@email.com', '41987654324');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Felipe Alves', 'felipe.alves@email.com', '51987654325');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Juliana Rocha', 'juliana.rocha@email.com', '61987654326');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Marcos Costa', 'marcos.costa@email.com', '71987654327');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Larissa Ferreira', 'larissa.ferreira@email.com', '81987654328');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Giovana Alves', 'giovana.alves@email.com', '91987654329');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Ricardo Souza', 'ricardo.souza@email.com', '02987654330');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Fernanda Lima', 'fernanda.lima@email.com', '12987654331');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Renato Gomes', 'renato.gomes@email.com', '22987654332');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Carla Pinto', 'carla.pinto@email.com', '32987654333');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Thiago Mendes', 'thiago.mendes@email.com', '42987654334');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Bianca Martins', 'bianca.martins@email.com', '52987654335');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Samuel Silva', 'samuel.silva@email.com', '62987654336');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Júlia Castro', 'julia.castro@email.com', '72987654337');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'André Souza', 'andre.souza@email.com', '82987654338');

INSERT INTO clientes (id_cliente, nome, email, telefone)
VALUES (seq_clientes.NEXTVAL, 'Isabela Oliveira', 'isabela.oliveira@email.com', '92987654339');

-- Inserir Serviços (5 registros)
INSERT INTO servicos (id_servico, nome_servico, descricao_servico, preco_servico)
VALUES (seq_servicos.NEXTVAL, 'Corte de Cabelo', 'Corte de cabelo masculino e feminino', 50.00);

INSERT INTO servicos (id_servico, nome_servico, descricao_servico, preco_servico)
VALUES (seq_servicos.NEXTVAL, 'Manicure', 'Serviço de manicure com esmalte', 30.00);

INSERT INTO servicos (id_servico, nome_servico, descricao_servico, preco_servico)
VALUES (seq_servicos.NEXTVAL, 'Pedicure', 'Serviço de pedicure com esmalte', 35.00);

INSERT INTO servicos (id_servico, nome_servico, descricao_servico, preco_servico)
VALUES (seq_servicos.NEXTVAL, 'Massagem', 'Massagem relaxante e terapêutica', 80.00);

INSERT INTO servicos (id_servico, nome_servico, descricao_servico, preco_servico)
VALUES (seq_servicos.NEXTVAL, 'Escova', 'Escova para cabelo liso e sedoso', 40.00);

-- Inserir Agendamentos (5 registros)
INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora)
VALUES (seq_agendamentos.NEXTVAL, 1, 1, 1, TO_TIMESTAMP('2024-11-18 14:00:00', 'YYYY-MM-DD HH24:MI:SS'));

INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora)
VALUES (seq_agendamentos.NEXTVAL, 2, 2, 2, TO_TIMESTAMP('2024-11-19 10:00:00', 'YYYY-MM-DD HH24:MI:SS'));

INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora)
VALUES (seq_agendamentos.NEXTVAL, 3, 3, 3, TO_TIMESTAMP('2024-11-20 09:30:00', 'YYYY-MM-DD HH24:MI:SS'));

INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora)
VALUES (seq_agendamentos.NEXTVAL, 4, 4, 4, TO_TIMESTAMP('2024-11-21 15:00:00', 'YYYY-MM-DD HH24:MI:SS'));

INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora)
VALUES (seq_agendamentos.NEXTVAL, 5, 1, 1, TO_TIMESTAMP('2024-11-22 11:00:00', 'YYYY-MM-DD HH24:MI:SS'));

-- Inserir Estoque (5 registros)
INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
VALUES (seq_estoque.NEXTVAL, 'Shampoo', 20, 'Shampoo para todos os tipos de cabelo', TO_DATE('2025-12-31', 'YYYY-MM-DD'), 15.00);

INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
VALUES (seq_estoque.NEXTVAL, 'Escova de Cabelo', 10, 'Escova de cabelo profissional', NULL, 30.00);

INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
VALUES (seq_estoque.NEXTVAL, 'Esmalte', 50, 'Esmalte vermelho', TO_DATE('2026-06-30', 'YYYY-MM-DD'), 5.00);

INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
VALUES (seq_estoque.NEXTVAL, 'Toalhas', 30, 'Toalhas para uso de salão', NULL, 10.00);

INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
VALUES (seq_estoque.NEXTVAL, 'Creme para Cabelos', 15, 'Creme hidratante para cabelos', TO_DATE('2025-11-01', 'YYYY-MM-DD'), 25.00);


SELECT * FROM agendamentos;
ALTER TABLE agendamentos ADD (status VARCHAR2(20));


-- Criar o usuário 'teste' com senha e tipo 'adm'
INSERT INTO usuarios (id_usuario, nome, senha, tipo_usuario)
VALUES (seq_usuarios.NEXTVAL, 'teste', '1234', 'adm');

