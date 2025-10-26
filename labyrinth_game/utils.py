# labyrinth_game/utils.py
import math as ma

from .constants import COMMANDS, EVENT_COUNT, EVENT_PROBABILITY, NUMBERS, ROOMS


# Функция описания текущей комнаты
def describe_current_room(game_state: dict) -> None:
  '''
  game_state - текущее состояние игры
  '''
  current_player_room = game_state['current_room']
  current_room_info = ROOMS[current_player_room]
  
  print(f"== {current_player_room.upper()} ==")
  
  if len(current_room_info['items']) > 0:
    print(f"Заметные предметы: {current_room_info['items']}")
  else:
    print("В комнате не видно никаких предметов.")
    
  print(f"Выходы: {current_room_info['exits']}")
  
  if current_room_info['puzzle'] is not None:
    print("Кажется, здесь есть загадка (используйте команду solve).")
    
# Функция решения загадки
def solve_puzzle(game_state: dict) -> None:
  '''
  game_state - текущее состояние игры
  '''
  if ROOMS[game_state['current_room']]['puzzle'] is None:
    print("Загадок здесь нет.")
    
  else:
    print(f"{ROOMS[game_state['current_room']]['puzzle'][0]}")
    users_answer = input("Ваш ответ: ")
    
    if (users_answer.lower() == ROOMS[game_state['current_room']]['puzzle'][1].lower() or ROOMS[game_state['current_room']]['puzzle'][1] in NUMBERS and NUMBERS[ROOMS[game_state['current_room']]['puzzle'][1]] == users_answer.lower()): # noqa: E501
      print("Загадка решена правильно!")
      ROOMS[game_state['current_room']]['puzzle'] = None
      
      if game_state['current_room'] == "hall":
        game_state['player_inventory'].append('torch')
        
      elif game_state['current_room'] == "trap_room":
        game_state['player_inventory'].append('coin')
      
      elif game_state['current_room'] == "library":
        game_state['player_inventory'].append('long_sword')
      
      print(f"Ваша награда: {game_state['player_inventory'][-1]}")
      
    else:
        
      
      if game_state['current_room'] == "trap_room":
        trigger_trap(game_state=game_state)
        
      else:
        print("Неверно. Попробуйте снова.")
      
# Функция попытки открытия сундука с сокровищами
def attempt_open_treasure(game_state: dict) -> None:
  '''
  game_state - текущее состояние игры
  '''
  if "treasure_key" in game_state['player_inventory']:
    print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
    ROOMS[game_state['current_room']]['items'].remove('treasure_chest')
    print("В сундуке сокровище! Вы победили!")
    game_state['game_over'] = True
    
  else:
    users_answer = input("Сундук заперт. ... Ввести код? (да/нет) ")
    
    if users_answer.lower() == "да":
      users_code = input("Введние код: ")
      
      if users_code == ROOMS[game_state['current_room']]['puzzle'][1]:
        print("Вы правильно вводите код, и замок щёлкает. Сундук открыт!")
        ROOMS[game_state['current_room']]['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
      
      else:
        print("Вы ввели неверный код, попробуйте еще раз.")
        
    else:
      print("Вы отступаете от сундука.")
    
# Функция отображения помощи
def show_help(commands_list: dict = COMMANDS) -> None:
  '''
  commands_list - список команд
  '''
  print("\nДоступные команды:")
  str_lens = [len(list(commands_list.keys())[i]) for i in range(0, len(commands_list))]
  max_str_len = max(str_lens)
  
  for command in commands_list:
    print(command + ': ' + ' ' * (max_str_len - len(command)) + commands_list[command])
    
# Функция генерации "случайных" чисел
def pseudo_random(seed: int, modulo: int) -> int:
  '''
  seed - количество шагов,
  modulo - целое число для определения диапазона результата
  '''
  rng_number = ma.sin(seed) * 12.9898 * 43758.5453
  rng_number_final = round((rng_number - ma.floor(rng_number)) * modulo)
  print(f"Сучайере число: {rng_number_final}")
  
  return rng_number_final

# Функция имитации срабатывания ловушки в комнате
def trigger_trap(game_state: dict) -> None:
  '''
  game_state - текущее состояние игры
  '''
  print("Ловушка активирована! Пол стал дрожать...")
  
  if len(game_state['player_inventory']) > 0:
    rng_item_index = pseudo_random(seed=game_state['steps_taken'], modulo=len(game_state['player_inventory'])-1) # noqa: E501
    deleted_item = game_state['player_inventory'].pop(rng_item_index)
    print(f"Вы смогли выбраться, но в процессе потеряли {deleted_item}.")
    
  else:
    rng_damage = pseudo_random(seed=game_state['steps_taken'], modulo=9)
    
    if rng_damage < 3:
    
      if "old_armor" in game_state['player_inventory']:
        print("Вам повезло, что на вас были старые доспехи. Вы избежали смертельного урона.") # noqa: E501
        print("Ваши доспехи сломались.")
        game_state['player_inventory'].remove('old_armor')
        
      else: 
        print("Вы не успеваете увернуться, и на вас падает каменная плита. Игра окончена!") # noqa: E501
        game_state['game_over'] = True
      
    else:
      print("Вы успеваете увернуться от падающей плиты.")
  
# Функция случайных событий
def random_event(game_state: dict) -> None:
  rng_event_trigger = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_PROBABILITY) # noqa: E501
  
  if rng_event_trigger < 6:
    rng_event_number = pseudo_random(seed=game_state['steps_taken'], modulo=EVENT_COUNT) # noqa: E501
    
    if rng_event_number == 0:
      print("Вы замечаете что-то блестящее на полу, это золотая монета (coin).")
      print("Вы подбираете монету.")
      game_state['player_inventory'].append('coin')
      
    elif rng_event_number == 1:
    
      print("Вы слышите шорох в темном углу комнаты. Ваш пульс заметно учащается.")
      if "sword" in game_state['player_inventory']:
        print("Вы обнажаете свой меч. Существо с гортанным рыком пятится назад и скрывается темноте.") # noqa: E501
        
      else:
        print("Существо прыгает на вас, но вы успеваете увернуться, после чего монстр скрывается в темноте.") # noqa: E501
        
    elif rng_event_number == 2:
    
      if game_state['current_room'] == "trap_room" and ("torch" not in game_state['player_inventory']): # noqa: E501
        trigger_trap(game_state=game_state)
        
        
