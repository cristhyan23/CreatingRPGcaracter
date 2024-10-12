### **Gerador de Respostas Detalhadas com a API Gemini**

**Introdução**

Este repositório contém um script Python que utiliza a API Gemini do Google para gerar respostas detalhadas a perguntas sobre um determinado tema. O script é capaz de analisar textos com marcações HTML e fornecer respostas completas, incluindo interpretação, resposta e justificativa.

**Pré-requisitos**

* **Python:** Versão 3.6 ou superior.
* **Bibliotecas:** `google-generativeai`, `os`, `dotenv`.
* **Conta Google Cloud:** Para obter a API Key.

**Instalação**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/cristhyan23/AiReplyQuests

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Ou venv\Scripts\activate no Windows
   ```

**Configuração**

1. **Obtenha a API Key:**
   * Acesse o console do Google Cloud e crie um projeto.
   * Ative a API Gemini.
   * Gere uma nova chave de API.
2. **Crie um arquivo `.env`:**
   * Na raiz do projeto, crie um arquivo chamado `.env` e adicione a seguinte linha, substituindo `YOUR_API_KEY` pela sua chave:
     ```
     API_KEY=YOUR_API_KEY
     ```
3. **Configure o tema:**
   * Modifique a variável `tema` no início do script para definir o tema sobre o qual as perguntas serão feitas.

**Utilização**

1. **Prepare o arquivo de perguntas:**
   * Crie um arquivo de texto chamado `Questoes.txt` e adicione as perguntas formatadas em HTML.
2. **Execute o script:**
   ```bash
   python ai_reply_quests.py
   ```
   O script gerará um arquivo `Respostas.txt` com as respostas detalhadas.

**Explicação do Código**

* **Importar bibliotecas:** Importa as bibliotecas necessárias para interagir com a API Gemini, manipular arquivos e carregar as variáveis de ambiente.
* **Configurar a API:** Configura a API Gemini com a chave obtida do arquivo `.env`.
* **Classe `AnalistaTexto`:**
    * **`__init__`:** Inicializa o modelo Gemini e configura a API.
    * **`melhorar_documentacao`:**
        * Cria um prompt detalhado para o modelo Gemini, incluindo a pergunta, instruções e exemplos.
        * Gera o conteúdo usando o modelo Gemini.
        * Formata a resposta e retorna o resultado.
* **Fluxo principal:**
    * Carrega as perguntas do arquivo `Questoes.txt`.
    * Cria uma instância da classe `AnalistaTexto`.
    * Chama a função `melhorar_documentacao` para gerar as respostas.
    * Salva as respostas no arquivo `Respostas.txt`.

**Considerações Finais**

* **Personalização:** Você pode personalizar o prompt para obter resultados diferentes, como alterar o nível de detalhamento das respostas ou adicionar restrições específicas.
* **Limitações:** A qualidade das respostas depende da qualidade das perguntas e do treinamento do modelo Gemini.
* **Melhorias:** Explore outras funcionalidades da API Gemini, como a geração de texto criativo ou a tradução de idiomas.

**Recursos Adicionais:**

* **Documentação da API Gemini:** [https://ai.google.dev/gemini-api/](https://ai.google.dev/gemini-api/)
