import random
import statistics
def carry_fans() -> tuple:
    # 1 stands for an American fan, 0 stands for a Dutch one
    fans = [1] * 11 + [0] * 7
    fans_carried_all = []
    while fans:
        # determine the first fan picked, remove them from the list of fans,
        # start the list of fans carried by the shuttle with them
        first_fan = random.choice(fans)
        fans.remove(first_fan)
        fans_carried = [first_fan]
        # pick fans until they are from the same team as the first one,
        # then add the list of them to the larger list (representing shuttles
        # of fans). If there are no fans left, break the loop.
        while True:
            try:
                fan = random.choice(fans)
            except IndexError:
                fans_carried_all += [fans_carried]
                break
            if fan == first_fan:
                fans.remove(first_fan)
                fans_carried += [fan]
            fans_carried_all += [fans_carried]
            break
    return fans_carried_all[-1][0], len(fans_carried_all)
def get_answers(simulations: int) -> tuple:
    americans_carried_last = []
    shuttles_used = []
    for _ in range(simulations):
        result = carry_fans()
        americans_carried_last += [result[0]]
        shuttles_used += [result[1]]
    return (statistics.mean(americans_carried_last),
            statistics.mean(shuttles_used))
print(get_answers(500000))
