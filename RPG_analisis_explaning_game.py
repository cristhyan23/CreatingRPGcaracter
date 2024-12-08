import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class AnalistaTexto:

    def __init__(self):
        self.gemini_model = 'gemini-1.5-flash'
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel(self.gemini_model)

    def melhorar_documentacao(self, caminho_arquivo, tema):
        # Upload do arquivo usando a File API
        try:
            arquivo = genai.upload_file(caminho_arquivo)
        except Exception as e:
            return f"Erro ao fazer upload do arquivo: {e}"

        # Gerar o conteúdo baseado no arquivo
        prompt = f"""
Você é um especialista em {tema}. O arquivo fornecido contém informações do jogo que você deve analisar.

**Sua missão:** me explicar de uma maneira extramente clara e simples todos os detalhes desse jogo e como o personagem abaixo pode jogar da melhor forma para vencer:

**Personagem: Caçador**

**Objetivos:**

1. Ganhar dinheiro para construir uma oficina.
2. Caçar a maior criatura assimilada.


**Análise de Atributos:**

* **Instintos:** O personagem tem alta Reação (2) e Percepção (2), indicando reflexos rápidos e boa capacidade de observação – atributos cruciais para um caçador.  A Potência (2) também é boa, sugerindo força física suficiente.  A baixa Sagacidade (1) pode ser um obstáculo, mas pode ser compensado com equipamentos e estratégia.
* **Práticas:**  Sua especialização em Armas (2) e Infiltração (2) é excelente para um caçador, permitindo tanto combate direto quanto aproximações furtivas.  A habilidade esportiva também é relevante.
* **Características:** Esquiva Precisa e Artes Marciais são ótimas para combate, enquanto Sentido de Sobrevivência aguçado auxilia na caça.
**Mutação:** Considerando os dois objetivos, uma mutação que combine habilidades de combate, sobrevivência e potencial de lucro seria ideal. A **Assimilação Silvestre** (5 de Copas)
* **Arco e Flecha (Letal e Duravel):**  Arma eficiente e silenciosa para caça furtiva, ideal para aproximações estratégicas, maximizando sua alta Reação e Infiltração.
Analise o conteúdo do arquivo e forneça recomendações detalhadas.
"""
        try:
            resposta = self.model.generate_content([prompt, arquivo])
            return resposta.text
        except Exception as e:
            return f"Erro ao gerar conteúdo: {e}"


if __name__ == "__main__":
    tema = 'RPG de mesa do jogo Assimilação RPG'
    caminho_arquivo = './Assimilacao_RPG_fastplay (SEM LORE).pdf'
    humaniza = AnalistaTexto()
    doc = humaniza.melhorar_documentacao(caminho_arquivo, tema)

    # Salvar o resultado em um arquivo texto
    with open('./resumo_do_jogo.txt', 'w', encoding='utf-8') as texto:
        texto.write(doc)
