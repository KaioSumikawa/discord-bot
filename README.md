# README - Discord Bot

Este e o meu projeto de bot para Discord desenvolvido para praticar configuracao de ambiente e integracao de APIs.

Criado para facilitar a gestao de tickets e exibicao de produtos em servidores.

---

## About

Este projeto foi criado para praticar:

- Criacao de repositorios e estruturacao de projetos
- Gerenciamento de variaveis de ambiente com arquivos .env
- Controle de versao e seguranca de tokens e chaves secretas
- Automacao de tarefas simples via comandos no Discord

---

## Configuracao Inicial

### 1. Clone o repositorio
```bash
git clone [https://github.com/KaioSumikawa/discord-bot.git](https://github.com/KaioSumikawa/discord-bot.git)
cd discord-bot
```
## Crie seu arquivo de configuracao (.env)
NUNCA compartilhe este arquivo! Ele contem suas chaves secretas. Crie um arquivo chamado .env na raiz do projeto com o seguinte conteudo:
``
DISCORD_TOKEN=seu_token_do_bot_aqui
``

## Obtenha seu token do Discord Bot
- Acesse o Discord Developer Portal.

- Selecione seu aplicativo.

- Va na secao Bot.

- Clique em Reset Token (se necessario).

- Copie o token gerado.

- Cole no seu arquivo .env no lugar de seu_token_do_bot_aqui.

## Instale as dependencias
- Use o pip para instalar as bibliotecas necessarias:
``
pip install discord.py python-dotenv
``
## Execute o bot
- Inicie o bot com o comando:
`` python main.py ``


