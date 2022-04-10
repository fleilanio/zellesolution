# Black-Scholes-Merton - Modelo de precificação de Call & Put Europeia

# Copyright (c) 2022 Francisco Costa
# MIT License - https://opensource.org/licenses/MIT
# Visite www.opcoesfacilitadas.com.br
from math import log, sqrt, exp
from scipy import stats


s0 = float(17.66)
k = 15.00
t = 69/252
r = 0.1175
sigma = 0.5186

def BSM_d1(s0, k, t, r, sigma):
    """
    Calcula o d1 da equação de Black-Scholes-Merton

    Inputs:
    s0: preço À vista do ativo

    k: strike da opção de compra

    t: tempo até o vencimento em dias

    r: taxa de juros livres de risco anual

    sigma: volatilidade histórica em termos anuais

    return: d1
    """
    d1 = (log(s0/k) + (r + 0.5*sigma**2)*t) / (sigma * sqrt(t))
    return d1

def BSM_d2(s0, k, t, r, sigma):
    """
    Calcula o d2 da equação de Black-Scholes-Merton

    Inputs:
    s0, k, t, r, sigma)
    """
    d2 = (log(s0 / k) + (r - 0.5 * sigma **2) * t) / (sigma * sqrt(t))
    return d2

d1 = BSM_d1(s0, k, t, r, sigma)
d2 = BSM_d2(s0, k, t, r, sigma)

def BSM_europeia(s0, k, t, r, d1, d2, tipo):
    """Função bsm_call(s0, k, t, r, sigma)
    Calcula o valor de uma opção de compra ou opção de venda europeia de acordo com o modelo de Black-Schoes-Merton
    Inputs:
    s0: preço À vista do ativo

    k: strike da opção de compra

    t: tempo até o vencimento em dias

    r: taxa de juros livres de risco anual

    sigma: volatilidade histórica em termos anuais

    tipo: define se o tipo é 'c' para call ou 'p' para put

    return: preço teórico da opção
    """
    
    if tipo == 'c':
        call = (s0 * stats.norm.cdf(d1, 0.0, 1.0)) - k * exp(-r * t) * stats.norm.cdf(d2, 0.0, 1.0)
        return call

    elif tipo == 'p':
        put = (k*exp(-r*t) * stats.norm.cdf(-d2, 0, 1.0)) - s0*stats.norm.cdf(-d1, 0, 1.0)
        return put

def BSM_delta(d1, tipo):
    """Calcula o DELTA de uma opção.
    Inputs:
    d1, tipo
    """
    if tipo == 'c':
        delta__call = stats.norm.cdf(d1, 0, 1.0)
        return delta__call
    elif tipo == 'p':
        delta_put = stats.norm.cdf(d1, 0, 1.0) - 1
        return delta_put

def BSM_theta(s0, k, t, r, sigma, d1, d2, tipo):
    """Calcula o THETA de uma opção.
    Inputs:
    s0, k, t, r, sigma, d1, d2
    """
    if tipo == 'c':
        theta_call = (-(s0*stats.norm.pdf(d1, 0, 1.0)*sigma) / (2 * sqrt(t))) \
                   - r*k*exp(-r*t)*stats.norm.pdf(d2, 0, 1.0)
        return theta_call / 365
    elif tipo == 'p':
        theta_put = (-(s0*stats.norm.pdf(d1, 0, 1.0)*sigma) / (2 * sqrt(t))) \
                  + r*k*exp(-r*t)*stats.norm.pdf(-d2, 0, 1.0)
        return theta_put /365
    
def BSM_gamma(s0, t, sigma, d1):
    """
    Calcula o GAMMA de uma opção.
    Inputs:
    s0, t, sigma, d1
    """
    gamma = stats.norm.pdf(d1, 0, 1.0) / (s0*sigma*sqrt(t))
    return gamma

def BSM_vega(s0, t, d1):
    """
    Calcula o vega te uma opção.
    Inputs:
    s0, t, d1
    """
    vega = s0*sqrt(t)*stats.norm.cdf(d1)
    return vega * 0.01

def BSM_rho(k, t, r, d2, tipo):
    """
    Calcula o RHO de uma opção.
    Inputs:
    k, t, r, d2, tipo
    """
    if tipo == 'c':
        rho_call = k*t*exp(-r*t)*stats.norm.cdf(d2)
        return rho_call * 0.01
    elif tipo == 'p':
        rho_put = -k*t*exp(-r*t)*stats.norm.cdf(-d2)
        return rho_put * 0.01

probabilidade = stats.norm.cdf(d2)
delta = BSM_delta(d1, tipo='c')
print('\n')
print('Delta da call:....................... %1.4f\n' % delta)

print('Probabilidade de exercício:.......... %1.4f\n' % probabilidade)

