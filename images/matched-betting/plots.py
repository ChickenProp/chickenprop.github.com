#! /usr/bin/python3

import sys
import os
import numpy as np
import pandas as pd
import plotnine as gg
import warnings
import matplotlib as mpl

# defaults
Cb = 0
Cl = 0.02


C = (1 - Cb) * (1 - Cl)

commission_string = 'C_b = %g, C_l = %g' % (Cb, Cl)

# math

def Pf_Ob_Ol(Pf):
    Ol = np.linspace(1, 10, 46)
    Ob = (Pf * (Ol - Cl) + C) / C

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'P_f': Pf})

def Pf_Ob_σ(Pf):
    σ = np.linspace(0, 5, 501)
    Ob = (Pf * (σ - Cl) + C) / (C - Pf)

    return pd.DataFrame({'σ': σ, 'O_b': Ob, 'P_f': Pf})

def Pq_Ob_Ol(Pq):
    Ol = np.linspace(1, 10, 46)
    Ob = ((Pq + 1) * (Ol - Cl) - Cb*(1 - Cl))/C

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'P_q': Pq})

def Pq_Ob_σ(Pq):
    σ = np.linspace(0, 5, 501)
    Λ = (Pq + 1)/(1 - Cl)
    Ob = (Λ*(σ - Cl) - Cb) / (1 - Cb - Λ)

    return pd.DataFrame({'σ': σ, 'O_b': Ob, 'P_q': Pq})

def Opr_Ob_Ol(Opr):
    Pf = Opr_Pf(Opr)
    return Pf_Ob_Ol(Pf).assign(Opr=Opr)

def Opr_Ob_σ(Opr):
    Pf = Opr_Pf(Opr)
    return Pf_Ob_σ(Pf).assign(Opr=Opr)

def Opr_Pf(Opr):
    return C * (Opr - 1)/(Opr - Cl)

def σpr_Ob_σ(σpr):
    Pq = σpr_Pq(σpr)
    return Pq_Ob_σ(Pq).assign(σpr=σpr)

def σpr_Pq(σpr):
    return (1 - Cl) / (1 - Cl + σpr) - 1

# helpers

def dollars(s):
    return '$%s$' % (s,)

def titles(t, s=commission_string): # title, hacky subtitle
    return gg.ggtitle('$%s$\n${}_{%s}$' % (t, s))

def colors(name):
    return gg.scale_color_hue(name=dollars(name),
                              labels=lambda l: ['%.1f' % x for x in l])

def labs(x, y):
    return gg.labs(x=dollars(x), y=dollars(y))

def limits(x, y=None, xbreaks=None, ybreaks=None):
    if y is None:
        y = x

    x0, x1 = x
    y0, y1 = y

    if xbreaks is None:
        xbreaks = np.linspace(x0, x1, x1 - x0 + 1)
    if ybreaks is None:
        ybreaks = np.linspace(y0, y1, y1 - y0 + 1)

    return [ gg.scale_x_continuous(limits=x, breaks=xbreaks),
             gg.scale_y_continuous(limits=y, breaks=ybreaks) ]

def savepath(basename):
    return os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),
                        basename)

def concat_map(f, cat, l):
    ret = pd.concat((f(x) for x in l), ignore_index=True)
    ret[cat] = pd.Categorical(ret[cat], ordered=True)
    return ret

def save_both(plot, basename):
    plot.save(savepath('%s.png' % (basename,)))
    plot.save(savepath('%s.small.png' % (basename,)),
              width=2.4, height=1.8)

def main():
    mpl.rc('mathtext', fontset='cm')

    warnings.filterwarnings('ignore', r'geom_\w+: Removed \d+ rows')
    warnings.filterwarnings('ignore', r'Saving .+ x .+ in image')
    warnings.filterwarnings('ignore', r'Filename: .+\.png')

    df = concat_map(Pf_Ob_Ol, 'P_f', np.linspace(0.1, 1, 10))
    save_both(gg.ggplot(df, gg.aes('O_b', 'O_l', group='P_f', color='P_f'))
              + titles('P_f(O_b, O_l)')
              + colors('P_f')
              + labs('O_b', 'O_l')
              + limits((1, 10))
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              + gg.geom_line()
              , 'Pf_Ob_Ol')

    df = concat_map(Pf_Ob_σ, 'P_f', np.linspace(0.1, 1, 10))
    save_both(gg.ggplot(df, gg.aes('O_b', 'σ', group='P_f', color='P_f'))
              + titles('P_f(O_b, σ)')
              + colors('P_f')
              + labs('O_b', 'σ')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Pf_Ob_σ')

    df = concat_map(Pq_Ob_Ol, 'P_q', np.linspace(-0.9, 0, 10))
    save_both(gg.ggplot(df, gg.aes('O_b', 'O_l', group='P_q', color='P_q'))
              + titles('P_q(O_b, O_l)')
              + colors('P_q')
              + labs('O_b', 'O_l')
              + limits((1, 10))
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              + gg.geom_line()
              , 'Pq_Ob_Ol')

    df = concat_map(Pq_Ob_σ, 'P_q', np.linspace(-0.9, 0, 10))
    save_both(gg.ggplot(df, gg.aes('O_b', 'σ', group='P_q', color='P_q'))
              + titles('P_q(O_b, σ)')
              + colors('P_q')
              + labs('O_b', 'σ')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Pq_Ob_σ')

    df = concat_map(Opr_Ob_Ol, 'Opr', np.linspace(1, 5, 9))
    save_both(gg.ggplot(df, gg.aes('O_b', 'O_l', group='Opr', color='Opr'))
              + titles("O'(O_b, O_l)")
              + colors("O'")
              + labs('O_b', 'Ol')
              + limits((1, 10), (1, 10))
              + gg.geom_line()
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              , 'Opr_Ob_Ol')

    df = concat_map(Opr_Ob_σ, 'Opr', np.linspace(1, 5, 9))
    save_both(gg.ggplot(df, gg.aes('O_b', 'σ', group='Opr', color='Opr'))
              + titles("O'(O_b, σ)")
              + colors("O'")
              + labs('O_b', 'σ')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Opr_Ob_σ')

    df = (pd.DataFrame({'Opr': np.linspace(1, 20, 91)})
            .assign(Pf=lambda x: Opr_Pf(x.Opr)))
    save_both(gg.ggplot(df, gg.aes('Opr', 'Pf'))
              + titles("P_f(O')")
              + labs("O'", 'P_f')
              + limits((1, 20), (0, 1),
                       xbreaks=np.linspace(2, 20, 10),
                       ybreaks=np.linspace(0, 1, 11))
              + gg.geom_line()
              + gg.geom_hline(yintercept=C, linetype='dashed', color='grey')
              , 'Pf_Opr')

    df = concat_map(σpr_Ob_σ, 'σpr', np.linspace(0, 5, 11))
    save_both(gg.ggplot(df, gg.aes('O_b', 'σ', group='σpr', color='σpr'))
              + titles("σ'(O_b, σ)")
              + colors("σ'")
              + labs('O_b', 'σ')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'σpr_Ob_σ')

    df = (pd.DataFrame({'σpr': np.linspace(0, 20, 101)})
            .assign(Pq=lambda x: σpr_Pq(x.σpr)))
    save_both(gg.ggplot(df, gg.aes('σpr', 'Pq'))
              + titles("P_q(σ')")
              + labs("σ'", 'P_q')
              + limits((0, 20), (-1, 0),
                       xbreaks=np.linspace(0, 20, 11),
                       ybreaks=np.linspace(-1, 0, 11))
              + gg.geom_line()
              , 'Pq_σpr')

if __name__ == '__main__':
    main()
