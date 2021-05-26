import random
from new_node import New_Node
from linkedlist import LinkedList


if __name__ == '__main__':

    linked_list = LinkedList()
    new_node = New_Node(1)

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.add_to_beginning(44)
    new_node.insert(5)


class Sweepstakes:
    contestant = {
            1: "Jason Voorhees",

            2:  "Freddy Kruger",

            3: "Michael Myers",

            4: "Pin Head",

            5: "Leather Face",

        }

    winner = random.choice(list(contestant.values()))
    print(f'The winner is {winner}!!!')


family = {
        'wife': 'Elsa Jordan',
        'son': 'Noah Jordan',
        'youngest_son': 'Jonah Jordan',
}





