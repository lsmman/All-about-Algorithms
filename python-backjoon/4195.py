class Friend_network():
    def __init__(self):
        self.network = list()
        self.person2network = {}
        self.last_network = 0
        self.network_cnt = []
        return
    
    def get_network_id(self, person):
        if person not in self.person2network:
            self.person2network[person] = -1
        team = self.person2network[person]
        return team

    def add_network(self):
        network_id = self.last_network
        self.network.insert(network_id, list())
        self.network_cnt.insert(network_id, 0)
        self.last_network += 1
        return network_id

    def add_member_in_network(self, person, network_id):
        self.person2network[person] = network_id
        self.network[network_id].append(person)
        self.network_cnt[network_id] += 1
    
    def make_network_empty(self, network_id):
        self.network[network_id] = []
        self.network_cnt[network_id] = 0

    def count_friend_network(self, conn):
        if len(conn) != 2:
            return 0
        
        person_a, person_b = conn
        network_a = self.get_network_id(person_a)
        network_b = self.get_network_id(person_b)

        if network_a == -1 and network_b == -1:
            new_network_id = self.add_network()
            self.add_member_in_network(person_a, new_network_id)
            self.add_member_in_network(person_b, new_network_id)
            return self.network_cnt[new_network_id]

        elif network_a == -1:
            self.add_member_in_network(person_a, network_b)
            return self.network_cnt[network_b]

        elif network_b == -1:
            self.add_member_in_network(person_b, network_a)
            return self.network_cnt[network_a]

        elif network_a == network_b:
            return self.network_cnt[network_a]

        from_ = max(network_a, network_b)
        to = min(network_a, network_b)
        for person_from in self.network[from_]:
            self.add_member_in_network(person_from, to)
        self.make_network_empty(from_)
        return self.network_cnt[to]

def main():
    answers = []
    T = int(input())
    for t in range(T):
        network = Friend_network()
        for _connection in range(int(input())):
            conn = input().split()
            cnt = network.count_friend_network(conn)
            answers.append(cnt)

    for ans in answers:
        print(ans)

# main()

def test():
    test1()
    test2()

def test1():
    # given
    conns = [
        "Fred Barney",
        "Barney Betty",
        "Betty Wilma",
    ]
    network = Friend_network()
    answers = []
    # when
    for conn in conns:
        result = network.count_friend_network(conn.split())
        answers.append(result)

    # then
    print(answers == [2,3,4])

def test2():
    # given
    conns = [
        "Fred Barney",
        "Betty Wilma",
        "Barney Betty",
    ]
    network = Friend_network()
    answers = []
    # when
    for conn in conns:
        result = network.count_friend_network(conn.split())
        answers.append(result)

    # then
    print(answers == [2,2,4])

# main()
test()