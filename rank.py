#!/usr/bin/env python3

import os

result = 'results.csv'

def rank():
    standings = {}
    try:
        res = open(result, 'rt')
        allraces = res.readlines()
        for player in os.listdir('bets/'):
            try:
                score = 0
                sc = open("bets/%s" % player, 'rt')
                allbet = sc.readlines()
                for idx in range(len(allraces)):
                    riders = allbet[idx].strip().split(',')
                    races = allraces[idx].strip().split(',')
                    for r in range(len(riders)):
                        if riders[r] in races:
                            # We get one point if rider is on the podium
                            score += 1
                        if riders[r] == races[r]:
                            # We get extra points on top if we guess the result of the rider
                            # 3 for first
                            # 2 for second
                            # 1 for third
                            score += (3-r)
                standings[player] = score
            except Exception as e:
                print('You are Fired %s' % e)
            finally:
                sc.close()
    except Exception as e:
        print('Unable to open results, try again %s' % e)
        return standings
    finally:
        res.close()
    return standings


if __name__ == "__main__":
    res = rank()
    r = sorted( ((s, p) for p, s in res.items()), reverse=True)
    for p in r:
        print("Player %s has %s points" % (p[1].capitalize(), p[0]))

