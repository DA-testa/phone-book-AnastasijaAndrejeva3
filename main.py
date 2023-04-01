# Anastasija Andrejeva, 18. grupa, 221RDC028
class Query:
    def __init__(self):
        self.book = {}

    def add(self, number, name):
        self.book[number] = name

    def delete(self, number):
        if number in self.book and self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        name = self.book.get(number)
        if name is None:
            return "not found"
        else:
            return name

def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]

def write_responses(contacts):
    print('\n'.join(contacts))

def process_queries(queries):
    contacts = []
    hash_table = Query()
    for query in queries:
        query_type = query[0]
        if query_type == 'add':
            number = int(query[1])
            name = query[2]
            hash_table.add(number, name)
        elif query_type == 'del':
            number = int(query[1])
            hash_table.delete(number)
        else:
            number = int(query[1])
            response = hash_table.find(number)
            contacts.append(response)
    return contacts

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

