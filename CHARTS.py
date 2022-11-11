import math
from itertools import cycle

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas

matplotlib.rcParams.update({'font.size': 6})


def get_line_style():
    ls_tuple = [
        ('solid', (0, ())),
        ('loosely dotted', (0, (1, 4))),
        ('dotted', (0, (1, 2))),
        ('densely dotted', (0, (1, 1))),

        ('loosely dashed', (0, (5, 4))),
        ('dashed', (0, (5, 2))),
        ('densely dashed', (0, (5, 1))),

        ('loosely dashdotted', (0, (3, 4, 1, 4))),
        ('dashdotted', (0, (3, 2, 1, 2))),
        ('densely dashdotted', (0, (3, 1, 1, 1))),

        ('loosely dashdotdotted', (0, (3, 4, 1, 4, 1, 4))),
        ('dashdotdotted', (0, (3, 2, 1, 2, 1, 2))),
        ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))
    ]

    for v in cycle(ls_tuple):
        yield v[1]


# only for alpha_b=0
def compute_axial_compression(lmd: float, kffy: float, an: float):
    ln = max(lmd * math.sqrt(kffy / 250), 13.5)
    eta = 0.00326 * (ln - 13.5)
    factor = (ln / 90) ** 2
    zeta = .5 * (factor + 1 + eta) / factor
    ac = zeta * (1 - math.sqrt(1 - (1 / zeta / zeta / factor)))
    return .9 * ac * kffy * an / 1000


def ub_strong_axis():
    ls = get_line_style()

    le = np.linspace(0, 20, 2000, endpoint=False)

    figure = plt.figure(figsize=(6.2, 9.4), dpi=200)

    UB = pandas.read_csv('REF/UB.DESIGNATION.csv')
    for i in UB['designation']:
        section = UB[i == UB['designation']]
        r_x = float(section['r_x'].values[0])
        f_y = float(section['f_y'].values[0])
        k_f = float(section['k_f'].values[0])
        A = float(section['A'].values[0])
        nc = [compute_axial_compression(l * 1000 / r_x, k_f * f_y, A) for l in le]
        plt.plot(le, nc, label=i, linestyle=next(ls), linewidth=1)

    plt.legend(ncol=2)
    plt.xlim(0, 20)
    plt.minorticks_on()
    plt.title('Grade 300 UB Strong Axis Compression', fontweight='bold')
    plt.xlabel('Effective Length [m]')
    plt.ylabel(r'$\phi{}N_c$ [kN]')
    plt.yscale('log')
    plt.grid(which='both')
    figure.tight_layout()
    figure.savefig('REF/UB.STRONG.NC.pdf')


def ub_weak_axis():
    ls = get_line_style()

    le = np.linspace(0, 10, 1000, endpoint=False)

    figure = plt.figure(figsize=(6.2, 9.4), dpi=200)

    UB = pandas.read_csv('REF/UB.DESIGNATION.csv')
    for i in UB['designation']:
        section = UB[i == UB['designation']]
        r_y = float(section['r_y'].values[0])
        f_y = float(section['f_y'].values[0])
        k_f = float(section['k_f'].values[0])
        A = float(section['A'].values[0])
        nc = [compute_axial_compression(l * 1000 / r_y, k_f * f_y, A) for l in le]
        plt.plot(le, nc, label=i, linestyle=next(ls), linewidth=1)

    plt.legend(ncol=2)
    plt.xlim(0, 10)
    plt.minorticks_on()
    plt.title('Grade 300 UB Weak Axis Compression', fontweight='bold')
    plt.xlabel('Effective Length [m]')
    plt.ylabel(r'$\phi{}N_c$ [kN]')
    plt.yscale('log')
    plt.grid(which='both')
    figure.tight_layout()
    figure.savefig('REF/UB.WEAK.NC.pdf')


def uc_strong_axis():
    ls = get_line_style()

    le = np.linspace(0, 20, 2000, endpoint=False)

    figure = plt.figure(figsize=(6.2, 9.4), dpi=200)

    UC = pandas.read_csv('REF/UC.DESIGNATION.csv')
    for i in UC['designation']:
        section = UC[i == UC['designation']]
        r_x = float(section['r_x'].values[0])
        f_y = float(section['f_y'].values[0])
        k_f = float(section['k_f'].values[0])
        A = float(section['A'].values[0])
        nc = [compute_axial_compression(l * 1000 / r_x, k_f * f_y, A) for l in le]
        plt.plot(le, nc, label=i, linestyle=next(ls), linewidth=1)

    plt.legend(ncol=2)
    plt.xlim(0, 20)
    plt.minorticks_on()
    plt.title('Grade 300 UC Strong Axis Compression', fontweight='bold')
    plt.xlabel('Effective Length [m]')
    plt.ylabel(r'$\phi{}N_c$ [kN]')
    plt.yscale('log')
    plt.grid(which='both')
    figure.tight_layout()
    figure.savefig('REF/UC.STRONG.NC.pdf')


def uc_weak_axis():
    ls = get_line_style()

    le = np.linspace(0, 10, 1000, endpoint=False)

    figure = plt.figure(figsize=(6.2, 9.4), dpi=200)

    UC = pandas.read_csv('REF/UC.DESIGNATION.csv')
    for i in UC['designation']:
        section = UC[i == UC['designation']]
        r_y = float(section['r_y'].values[0])
        f_y = float(section['f_y'].values[0])
        k_f = float(section['k_f'].values[0])
        A = float(section['A'].values[0])
        nc = [compute_axial_compression(l * 1000 / r_y, k_f * f_y, A) for l in le]
        plt.plot(le, nc, label=i, linestyle=next(ls), linewidth=1)

    plt.legend(ncol=2)
    plt.xlim(0, 10)
    plt.minorticks_on()
    plt.title('Grade 300 UC Weak Axis Compression', fontweight='bold')
    plt.xlabel('Effective Length [m]')
    plt.ylabel(r'$\phi{}N_c$ [kN]')
    plt.yscale('log')
    plt.grid(which='both')
    figure.tight_layout()
    figure.savefig('REF/UC.WEAK.NC.pdf')


if __name__ == '__main__':
    ub_strong_axis()
    ub_weak_axis()
    uc_strong_axis()
    uc_weak_axis()
