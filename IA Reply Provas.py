import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class AnalistaTexto:

    def __init__(self):
        self.gemini_model = 'gemini-1.5-flash'
        genai.configure(api_key=os.environ["API_KEY"])
        # The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
        self.model = genai.GenerativeModel(self.gemini_model)
    
    def melhorar_documentacao(self,texto,tema):
        prompt = f"""Você é um especialista em {tema} e recebeu uma prova com 10 perguntas marcadas com tags HTML

    aqui está prova {texto}
    Sua missão é responder corretamente a todas as perguntas.

 """
        resposta = self.model.generate_content(
            [prompt],
            stream=True
        )
        resposta.resolve()
        resultado = ""
        try:
            resultado = resposta.text
        except ValueError:
            return "Não foi possível gerar o roteiro"
        if resultado:
            return resultado


if __name__ == "__main__":
    tema = ''
    humaniza = AnalistaTexto()
    resultado = ''
    with open(r'./Questoes.txt','r', newline="", encoding="utf-8", errors="replace") as texto:
        resultado = texto.readlines()

    doc = humaniza.melhorar_documentacao(resultado,tema)
    with open(r'./Respostas','w',encoding="utf-8") as texto:
        texto.write(doc)