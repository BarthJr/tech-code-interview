"""
>>> user = User()
>>> user.t_task
4
>>> user.tick()
>>> user.tick()
>>> user.tick()
>>> user.t_task
1
>>> user.tick()
>>> user.t_task
0
>>> user.tick()
>>> user.t_task
0
>>> server = Server()
>>> server.add_user()
>>> server.users
[4]
>>> server.tick()
>>> server.add_user()
>>> server.users
[3, 4]
>>> server.tick()
>>> server.tick()
>>> server.tick()
>>> server.users
[1]
>>> server.tick()
>>> server.users
[]
>>> load_balancer = LoadBalancer()
>>> load_balancer.add_users(3)
>>> load_balancer
2,1
>>> load_balancer.tick()
>>> load_balancer.tick()
>>> load_balancer.tick()
>>> load_balancer.add_users(2)
>>> load_balancer
2,2,1
>>> load_balancer.tick()
>>> load_balancer
1,1
>>> load_balancer
1,1
>>> load_balancer.have_servers()
True
>>> load_balancer.tick()
>>> load_balancer.tick()
>>> load_balancer.tick()
>>> load_balancer.have_servers()
False
"""


class LoadBalancer:
    def __init__(self, t_task: int = 4, u_max: int = 2):
        self.t_task = t_task
        self.u_max = u_max
        self.servers = []
        self.cost = 0

    def tick(self):
        for server in self.servers:
            server.tick()
        self.cost += len(self)
        self.servers = [server for server in self.servers if not server.is_empty()]

    def add_users(self, number_users: int):
        for server in self.servers:
            while not server.is_full() and number_users > 0:
                server.add_user()
                number_users -= 1
        if number_users > 0:
            self.servers.append(Server(self.u_max, self.t_task))
            self.add_users(number_users)

    def have_servers(self) -> bool:
        return bool(self.servers)

    def __repr__(self) -> str:
        return ','.join(str(s) for s in self.servers)

    def __len__(self):
        return len(self.servers)


class Server:
    def __init__(self, u_max: int = 2, t_task: int = 4):
        self.users = []
        self.u_max = u_max
        self.t_task = t_task

    def tick(self):
        for user in self.users:
            user.tick()
        self.users = [user for user in self.users if not user.is_ended()]

    def is_full(self) -> int:
        return len(self.users) >= self.u_max

    def is_empty(self) -> int:
        return len(self.users) == 0

    def add_user(self):
        self.users.append(User(self.t_task))

    def __repr__(self) -> str:
        return f'{len(self.users)}'


class User:
    def __init__(self, t_task: int = 4):
        self.t_task = t_task

    def tick(self):
        if self.t_task:
            self.t_task -= 1

    def is_ended(self) -> bool:
        return self.t_task == 0

    def __repr__(self) -> str:
        return f'{self.t_task}'


if __name__ == '__main__':
    try:
        with open('input.txt') as f:
            file = open('output.txt', 'w')
            ttask = int(f.readline())
            umax = int(f.readline())
            load_balancer = LoadBalancer(ttask, umax)
            for line in f:
                load_balancer.add_users(int(line))
                print(str(load_balancer), file=file)
                load_balancer.tick()
            while load_balancer.have_servers():
                print(str(load_balancer), file=file)
                load_balancer.tick()
            print(str(0), file=file)
            print(load_balancer.cost, file=file)
            file.close()
    except FileNotFoundError:
        line = None
