# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa_introducao = ['Oi', 'Olá', 'Tudo bem?', 'Tudo bem']
conversa_filme = ['Qual seu filme favorito', 'Não tenho filme favorito', 'Qual seu tipo de filme favorito?', 'Filmes de Ficção Científica']

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.portuguese"
)

#bot.train(conversa_introducao)
#bot.train(conversa_filme)

while 1:
    pergunta = input('Você: ')
    resposta = bot.get_response(pergunta)

    print('Bot: ', resposta)
