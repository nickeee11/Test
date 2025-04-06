import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

# Authentication
GROUP_ID = 'club229974801'
GROUP_TOKEN = 'vk1.a.CPy2spnDWiwwPibgqWVJcNkX7DOxcQcEDmx-EEHeVGzPuyX7CiN5KRQHhhg3uM40V5RUEuyvuh3QNlBK25Nof62B8SyoY0shh9kDChA0X3jjmA9z7IaKoMaonZDgcWH7WEhQWzQq4TWRbK-kFzpveTPzBvJgooFFA58AW3BBwfoVGafuEQBzESOV6pSAnEduC7Bb0GK8ieSDfgkEBHywyQ'

def main():
    vk_session = vk_api.VkApi(token=GROUP_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)

    print("Bot is running...")
    
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.object.message
            user_id = msg['from_id']
            text = msg['text'].lower()
            
            print(f"Received message: {text} from {user_id}")
            
            # Simple echo bot with some commands
            if text == 'привет':
                response = f"Привет, пользователь! 😊"
            elif text == 'команды':
                response = "Доступные команды: привет, команды, случайное число"
            elif text == 'случайное число':
                response = f"Ваше случайное число: {random.randint(1, 100)}"
            else:
                response = "Я не понимаю эту команду. Напишите 'команды' для списка команд."
            
            vk.messages.send(
                user_id=user_id,
                message=response,
                random_id=random.randint(0, 2**64)
            )

if __name__ == '__main__':
    main()
