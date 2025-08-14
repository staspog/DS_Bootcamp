import sys

def call_center(clients: list, recipients: list) -> list:
    """Клиенты, которые не видели промо-письмо."""
    return list(set(clients) - set(recipients))

def potential_clients(participants: list, clients: list) -> list:
    """Участники события, не являющиеся клиентами."""
    return list(set(participants) - set(clients))

def loyalty_program(clients: list, participants: list) -> list:
    """Клиенты, которые не участвовали в событии."""
    return list(set(clients) - set(participants))

def main():

    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
        'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
        'mr@robot.gov', 'eleven@yahoo.com'
    ]
    recipients = ['andrew@gmail.com', 'jessica@gmail.com']

    # Проверка аргументов
    if len(sys.argv) != 2:
        raise ValueError("Ошибка: требуется ровно один аргумент.")

    task = sys.argv[1]
    tasks = {
        'call_center': call_center,
        'potential_clients': potential_clients,
        'loyalty_program': loyalty_program
    }

    try:
        # Выбор задачи
        if task == 'call_center':
            result = tasks[task](clients, recipients)
        elif task == 'potential_clients':
            result = tasks[task](participants, clients)
        elif task == 'loyalty_program':
            result = tasks[task](clients, participants)
        else:
            raise ValueError("Неверное название задачи.")
        
        for email in result:
            print(email)
            
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()