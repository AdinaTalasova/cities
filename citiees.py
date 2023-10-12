# # Есть файл с названиями городов 
# cities.txt. 
# # Необходимо считать его и записать
# #  города в список. 
# # Затем попросить пользователя ввести
# #  название города
# # (регистр не должен учитываться, 
# # то есть Париж и париж
# #   считать одинаковыми). Если такого 
# # слова нет, сообщать
# # об этом пользователю. Если же есть, 
# # то поиграть в города.
# # Необходимо найти это слово в списке,
# # удалить его и 
# # поискать слово на последнюю букву.
# # Повторять это действие до тех пор 
# # пока в списке будут
# # подходящие слова. Последнее 
# # совпавшее слово вывести на экран.


f = open('cities.txt', 'r', encoding='utf-8') 
f1 = f.read()
cities2 = list(f1)
bot_answer = cities2.pop ()

# print ('bot: ' + bot_answer)
# print('to your letter"' + bot_answer [-1] + '".')


while True:
    user_answer = input ('your city for bot`s letter: ')
    if user_answer.lower() [0] != bot_answer [-1]:
        print (bot_answer)
        continue
    elif user_answer not in  f1:
        print ('this city is not exist. Try again')
    elif user_answer not in cities2:
        print ('this city is already was')
    else:
        print ('right!')
        print (f'to me with this letter {user_answer[-1]}.')
        cities2.remove (user_answer)

        for candidate in cities2:
            if candidate.lower()[0] == user_answer[-1]:
                bot_answer = candidate
                cities2.remove (candidate)
                print ('your city for bot`s letter: ' + candidate)
                print (f'to me with this letter {candidate [-1]}.')
                break
        else:
            game_over = True
            print (f'I do not know cities with this letter {user_answer[-1]}. You are win!')