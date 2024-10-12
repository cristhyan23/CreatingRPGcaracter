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
        prompt = f"""
Você é um especialista em {tema} e recebeu uma prova com 10 perguntas formatadas em tags HTML no formato de [HTML, XML, etc.].

**Prova:** {texto}

**Sua missão:** Responder a todas as perguntas de forma [básica, intermediária, avançada], apresentando as respostas em formato de lista numerada. Para cada pergunta, inclua:

* **Questão (Número):** A pergunta original, copiada exatamente como aparece na prova.
* **Interpretação:** Uma breve explicação da sua compreensão da pergunta, destacando qualquer ambiguidade.
* **Resposta:** A resposta correta e completa.
* **Justificativa:** Uma explicação detalhada do raciocínio por trás da resposta, incluindo referências a conceitos relevantes e exemplos.

**Exemplo de Resposta:**

1. **Questão (1):** Qual a capital da França?
   * **Interpretação:** A pergunta busca identificar a cidade principal da França.
   * **Resposta:** Paris.
   * **Justificativa:** Paris é a cidade mais populosa da França e sede do governo francês.

**Observação:** Caso a pergunta seja aberta ou tenha múltiplas respostas corretas, apresente todas as opções válidas e justifique sua escolha.

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
    tema = 'Engenharia de Software'
    humaniza = AnalistaTexto()
    resultado = ''
    with open(r'./Questoes.txt','r', newline="", encoding="utf-8", errors="replace") as texto:
        resultado = texto.readlines()

    doc = humaniza.melhorar_documentacao(resultado,tema)
    with open(r'./Respostas.txt','w',encoding="utf-8") as texto:
        texto.write(doc)