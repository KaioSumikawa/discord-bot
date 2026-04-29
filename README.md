# Discord Bot 

> Este projeto é um bot para Discord desenvolvido com foco em automação de processos, integração com APIs e boas práticas de Governança de TI, especialmente em relação a segurança, controle de acesso e gestão de configurações sensíveis.

## Objetivo do Projeto
O bot foi criado para simular cenários reais de sistemas em produção, com foco em:

* **Automação de tarefas** via comandos no Discord
* **Gestão de tickets** dentro de servidores
* **Exibição dinâmica** de produtos e informações
* **Práticas de segurança** com variáveis de ambiente
* **Separação** entre código e dados sensíveis

## Perspectiva de Governança de TI
Este projeto aplica conceitos básicos de Governança de TI, como:

* **Segurança da Informação**: Uso de .env para evitar exposição de credenciais no código-fonte.
* **Controle de Acesso (IAM básico)**: Tokens e permissões gerenciados externamente ao código.
* **Gestão de Configuração**: Separação entre ambiente de desenvolvimento e execução.
* **Rastreabilidade e versionamento**: Uso de Git para controle de mudanças no sistema.
* **Automação de processos operacionais**: Redução de tarefas manuais via comandos no Discord.


## Tecnologias Utilizadas
* Python
* discord.py
* python-dotenv
* API do Discord

## Configuração Inicial

### 1. Clone o repositório
```bash
git clone [https://github.com/KaioSumikawa/discord-bot.git](https://github.com/KaioSumikawa/discord-bot.git)
cd discord-bot
```
### 2. Configuração de variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

> [!IMPORTANT]
> **Aviso de Governança de TI:** Este arquivo contém credenciais sensíveis. **Nunca** compartilhe, versione ou exponha publicamente. Adicione `.env` ao seu `.gitignore`.

No arquivo `.env`, adicione:

```env
DISCORD_TOKEN=seu_token_do_bot_aqui
```
### 3. Obtenção do Token do Bot

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Selecione sua aplicação
3. Vá até a seção **Bot**
4. Clique em **Reset Token** (se necessário)
5. Copie o token gerado e insira no arquivo `.env`

### 4. Instalação das dependências

```bash
pip install discord.py python-dotenv
```

### 6. Execução do bot

```bash
python main.py
```

## Boas Práticas Aplicadas

- Não versionar arquivos `.env`
- Evitar hardcoding de credenciais no código
- Separação entre código e configuração
- Uso de bibliotecas oficiais e mantidas
- Princípio do menor privilégio para tokens

## Possíveis Evoluções (Visão de Governança)

- [ ] Implementação de logs estruturados (auditoria)
- [ ] Controle de permissões por role no Discord
- [ ] Monitoramento de uso do bot
- [ ] Integreção com banco de dados para histórico de tickets
- [ ] Pipeline CI/CD para deploy automatizado

**Desenvolvido por Kaio Sumikawa**
