class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def __repr__(self) -> str:
        return "Data: "  + self.data + "   Ptr: " + str(self.pointer)


linked_list_data = []
linked_list_data.append(Node("Empty" , 1))
linked_list_data.append(Node("Empty" , 2))
linked_list_data.append(Node("Empty" , 3))
linked_list_data.append(Node("Empty" , 4))
linked_list_data.append(Node("Empty" , -1))

start_pointer = -1

next_free_pointer = 0
print(linked_list_data)