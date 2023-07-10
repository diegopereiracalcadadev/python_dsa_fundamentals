# https://platform.openai.com/docs/api-reference/chat/create
# https://platform.openai.com/docs/guides/rate-limits

import openai

openai.api_key = "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"


def gera_texto(texto):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = texto,         # texto inicial da conversa
        max_tokens = 150,       # comprimento da resposta gerada
        n = 5,                  # qtas conclusões gerar para cada prompt
        stop = None,            # o texto retornado não conterá a sequência de parada
        temperature = 0.8,      # medida de aleatoriedade - 0 muito identificável, 1 muito aleatório
    )

def main():
    print("Manda ver... (digite sair, para sair)")

    while True:
        user_msg = input("\nVocê: ")

        if user_msg.lower() == "sair":
            break
        
        gpt4_prompt = f"Usuário: {user_msg}\nChatbot:"

        chatbot_response = gera_texto(gpt4_prompt)

        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()