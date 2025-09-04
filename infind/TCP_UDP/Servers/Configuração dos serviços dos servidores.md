# Documentação dos Serviços em Python com `systemd`

Esta documentação explica como configurar e gerenciar seus servidores Python de forma robusta em um ambiente Linux (como um Droplet da DigitalOcean). A configuração garante que os servidores rodem em segundo plano, iniciem automaticamente com o sistema e sejam reiniciados em caso de falha.

Para isso, usamos o **`systemd`**, o gerenciador de serviços padrão na maioria das distribuições Linux.

## 1\. Estrutura do Projeto

Certifique-se de que seus arquivos de servidor (`server.py` e `receiver.py`) e o arquivo de log (`log.txt`) estão organizados em um diretório específico. Por exemplo:

```bash
/home/seu_usuario/servidores_python/
├── server.py
├── receiver.py
├── log.txt
└── ...
```

## 2\. Criando os Arquivos de Serviço do `systemd`

Você precisa criar um arquivo de serviço (`.service`) para cada um dos seus servidores. Esses arquivos informam ao `systemd` como iniciar, parar e monitorar cada script.

### Servidor TCP (`server.py`)

Crie o arquivo de serviço para o servidor TCP:

```bash
sudo nano /etc/systemd/system/meu_servidor_tcp.service
```

Cole o seguinte conteúdo, substituindo **`/caminho/para/seus/arquivos`** pelo caminho real do seu projeto e **`seu_usuario`** pelo seu nome de usuário.

```ini
[Unit]
Description=Servidor TCP Multi-Cliente
After=network.target

[Service]
User=seu_usuario
WorkingDirectory=/caminho/para/seus/arquivos
ExecStart=/usr/bin/python3 /caminho/para/seus/arquivos/server.py
Restart=always
RestartSec=3
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=meu_servidor_tcp

[Install]
WantedBy=multi-user.target
```

### Servidor UDP (`receiver.py`)

Crie o arquivo de serviço para o servidor UDP:

```bash
sudo nano /etc/systemd/system/meu_servidor_udp.service
```

Cole o seguinte conteúdo, fazendo as mesmas substituições de caminho e nome de usuário:

```ini
[Unit]
Description=Servidor UDP Multi-Cliente
After=network.target

[Service]
User=seu_usuario
WorkingDirectory=/caminho/para/seus/arquivos
ExecStart=/usr/bin/python3 /caminho/para/seus/arquivos/receiver.py
Restart=always
RestartSec=3
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=meu_servidor_udp

[Install]
WantedBy=multi-user.target
```

**Parâmetros importantes:**

  * `Restart=always`: Este comando garante que o `systemd` reiniciará o serviço automaticamente se ele falhar ou travar.
  * `RestartSec=3`: Define um intervalo de 3 segundos antes de tentar reiniciar.
  * `StandardOutput=syslog`: Redireciona a saída padrão do seu script (como os `print()`) para os logs do sistema, facilitando a depuração.

## 3\. Gerenciando os Serviços

Após criar os arquivos de serviço, use os comandos `systemd` para controlá-los.

### Habilitar e Iniciar

1.  **Recarregue** o `systemd` para que ele reconheça os novos arquivos de serviço:

    ```bash
    sudo systemctl daemon-reload
    ```

2.  **Habilite** os serviços para que eles iniciem automaticamente toda vez que o Droplet for reiniciado:

    ```bash
    sudo systemctl enable meu_servidor_tcp.service
    sudo systemctl enable meu_servidor_udp.service
    ```

3.  **Inicie** os serviços imediatamente:

    ```bash
    sudo systemctl start meu_servidor_tcp.service
    sudo systemctl start meu_servidor_udp.service
    ```

### Verificando o Status

Para confirmar que os serviços estão rodando e em bom estado, use o comando `status`:

```bash
sudo systemctl status meu_servidor_tcp.service
sudo systemctl status meu_servidor_udp.service
```

A saída deve mostrar **`Active: active (running)`** em verde.

### Acessando os Logs

Para depurar problemas e ver a saída dos seus scripts em tempo real, use o `journalctl` com a opção `-f` (follow):

```bash
# Para o servidor TCP
sudo journalctl -f -u meu_servidor_tcp.service

# Para o servidor UDP
sudo journalctl -f -u meu_servidor_udp.service
```

Pressione `Ctrl + C` para sair do modo de visualização.

### Outros Comandos Úteis

  * **Parar um serviço:** `sudo systemctl stop meu_servidor_tcp.service`
  * **Reiniciar um serviço:** `sudo systemctl restart meu_servidor_tcp.service`
  * **Desabilitar um serviço:** `sudo systemctl disable meu_servidor_tcp.service`

Essa configuração garante que seus servidores rodarão de forma autônoma e confiável em seu Droplet, sem a necessidade de manter o terminal aberto.
