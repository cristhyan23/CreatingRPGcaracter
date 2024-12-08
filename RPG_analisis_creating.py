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

**Sua missão:** definir qual seria a melhor mutação para o personagem, considerando as seguintes características:
Posição do Social do Personagem: Medica Cientista
Proposito: 1 descobrir a origem da assimilação; 2- buscar conhecimento através da exploração.

Instintos: 1 reação, 2 percepção, 2 sagacidade, 1 potência, 1 influência, 2 resolução
Conhecimentos: 0 agrário, 2 biológico, 1 exato, 2 medicina, 1 social, 0 artístico
Práticas: 0 esportivas, 0 ferramentas, 0 ofícios, 1 armas, 0 veículos, 1 infiltração

Características:
- Primeiros Socorros
- Ciência Forense
- Memoria Afiada

Analise o conteúdo do arquivo e forneça recomendações detalhadas.
"""
        try:
            resposta = self.model.generate_content([prompt, arquivo])
            return resposta.text
        except Exception as e:
            return f"Erro ao gerar conteúdo: {e}"


if __name__ == "__main__":
    tema = 'Criar Personagem RPG de mesa do jogo Assimilação RPG'
    caminho_arquivo = './Assimilacao_RPG_fastplay (SEM LORE).pdf'

    humaniza = AnalistaTexto()
    doc = humaniza.melhorar_documentacao(caminho_arquivo, tema)

    # Salvar o resultado em um arquivo texto
    with open('./personagem.txt', 'w', encoding='utf-8') as texto:
        texto.write(doc)
