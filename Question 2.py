import Question as Cls

COIN_PROB = 0.4
N_FLIPS = 20

myCoin = Cls.Game(id=1, n_flips=N_FLIPS, coin_probability=COIN_PROB)

myCoin.simulate(N_FLIPS)

print(myCoin.get_expected_cost())
