#!/usr/bin/env python
# coding:utf-8
"""
Name    : agent.py
Author  : Matias Selser & Javier Kreiner
Desc    :
"""

import src.rl_trading.environment

def spread_func(beta, sigma, k):
    return lambda T_t: src.rl_trading.environment.spread(beta, sigma, T_t, k)


def r_func(sigma, beta):
    return lambda T_t, s, q: src.rl_trading.environment.r(beta, sigma, T_t, s, q)


class AvellanedaAgent:
    def __init__(self, beta, sigma, k):
        self.spread_func = spread_func(beta, sigma, k)
        self.r_func = r_func(sigma, beta)

    def act(self, observation):
        spread = self.spread_func(observation[2])
        r_ = self.r_func(observation[2], observation[0], observation[1])

        bid = r_ - spread / 2
        ask = r_ + spread / 2

        ds = observation[0] - r_

        # return spread, ds
        return ds

    def step(self, observation):
        return self.act(observation)


class SymmetricAgent:
    def __init__(self, beta, sigma, k):
        self.spread_func = spread_func(beta, sigma, k)

    def act(self, observation):
        # spread = self.spread_func(observation[2])
        return 0

    def step(self, observation):
        return self.act(observation)
