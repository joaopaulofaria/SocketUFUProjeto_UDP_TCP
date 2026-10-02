# Socket Projeto – Cifra de César com TCP e UDP

Projeto de comunicação em rede usando **sockets em Python**, com clientes e servidores nos protocolos **TCP** e **UDP**, executados em **containers Docker**.

O servidor **UDP** recebe uma palavra e a **criptografa** com a **Cifra de César** (deslocamento de 3). O servidor **TCP** faz o caminho inverso: recebe a mensagem criptografada e a **descriptografa**.

---

## Estrutura do projeto

```
socketprojetoufu/
├── socketTCPufu/
│   ├── dockerfile
│   ├── socketTCPclient.py
│   └── socketTCPserver.py
├── socketUDPufu/
│   ├── dockerfile
│   ├── socketudpclient.py
│   └── socketudpserver.py
├── docker-compose.yaml
└── README.md
```

---

## Como funciona

### Cifra de César (deslocamento 3)

Cada caractere da mensagem é substituído pelo caractere que está 3 posições à frente na tabela ASCII/Unicode.

| Original | Criptografado |
|----------|---------------|
| `a`      | `d`           |
| `b`      | `e`           |
| `abc`    | `def`         |

A descriptografia faz o processo contrário (deslocamento de -3).

### Fluxo da comunicação

1. O **cliente UDP** pede uma palavra ao usuário e a envia ao **servidor UDP**.
2. O **servidor UDP** aplica a cifra de César (+3) e devolve a mensagem criptografada.
3. O **cliente TCP** envia a mensagem criptografada ao **servidor TCP**.
4. O **servidor TCP** aplica o deslocamento inverso (-3) e devolve a mensagem original.

```
Cliente UDP ──(palavra)──────────► Servidor UDP
Cliente UDP ◄──(palavra cifrada)── Servidor UDP

Cliente TCP ──(palavra cifrada)──► Servidor TCP
Cliente TCP ◄──(palavra original)─ Servidor TCP
```

---

## Portas utilizadas

| Serviço  | Protocolo | Porta  | Container          |
|----------|-----------|--------|--------------------|
| Servidor TCP | TCP   | `1216` | `serversockettcp`  |
| Servidor UDP | UDP   | `4443` | `serversocketudp`  |

---

## Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/) e Docker Compose

---

## Como executar

### 1. Construir as imagens

Na raiz do projeto, construa as imagens usadas pelo `docker-compose.yaml`:

```bash
docker build -t sockettcp1216 ./socketTCPufu
docker build -t socketudp1216 ./socketUDPufu
```

### 2. Subir os servidores

```bash
docker compose up -d
```

Para acompanhar os logs:

```bash
docker compose logs -f
```

### 3. Executar os clientes

Em outro terminal, rode os clientes localmente:

```bash
# Cliente UDP (criptografa)
python socketUDPufu/socketudpclient.py

# Cliente TCP (descriptografa)
python socketTCPufu/socketTCPclient.py
```

> **Importante:** edite a variável `serverName` nos clientes com o IP da máquina onde os containers estão rodando (por exemplo, `serverName = '10.0.99.150'`). Se estiver testando na própria máquina, use `localhost`.

### 4. Encerrar

```bash
docker compose down
```

---

## Exemplo de uso

**Cliente UDP**

```
Digite sua senha para criptografia: abc
def
```

**Cliente TCP** (enviando a mensagem criptografada)

```
def  →  abc
```

---

## docker-compose.yaml

```yaml
services:
  serversockettcp:
    image: sockettcp1216
    container_name: serversockettcp
    ports:
      - '1216:1216'
    restart: unless-stopped

  serversocketudp:
    image: socketudp1216
    container_name: serversocketudp
    ports:
      - '4443:1216/udp'
    restart: unless-stopped
```

---

## Tecnologias

- Python 3 (módulo `socket`)
- Docker e Docker Compose
- Protocolos TCP e UDP

---

## Autor

Projeto desenvolvido para a disciplina de Redes de Computadores – UFU.
