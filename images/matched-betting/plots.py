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
    Ol = np.linspace(1, 10.5, 5)
    Ob = (Pf * (Ol - Cl) + C) / C

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'P_f': Pf})

def Pf_Ob_σ(Pf):
    σ = np.linspace(0, 5.5, 5)
    Ob = (Pf * (σ - Cl) + C) / (C - Pf)

    return pd.DataFrame({'σ': σ, 'O_b': Ob, 'P_f': Pf})

def Pq_Ob_Ol(Pq):
    Ob = np.linspace(1, 10.5, 5)
    Ol = (Ob*C + Cb*(1 - Cl))/(Pq + 1) + Cl

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'P_q': Pq})

def Pq_Ob_σ(Pq):
    Λ = (Pq + 1)/(1 - Cl)
    Ob = np.linspace(1, 10.5, 5)
    σ = (Ob*(1 - Cb - Λ) + Cb)/Λ + Cl

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

# The σ graphs from these aren't very good, but they don't appear inline in the
# post so whatever.
def liab_Ob_Ol_free(liab):
    Ol = np.linspace(1.01, 30.5, 1000)
    Ob = 1 + liab * (Ol - Cl) / ((Ol - 1) * (1 - Cb))
    σ = Ol - Ob

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'σ': σ, 'liab': liab})

def liab_Ob_Ol_qual(liab):
    Ol = np.linspace(1.01, 30.5, 1000)
    Ob = 1 - 1/(1 - Cb) + liab * (Ol - Cl) / ((Ol - 1) * (1 - Cb))
    σ = Ol - Ob

    return pd.DataFrame({'O_l': Ol, 'O_b': Ob, 'σ': σ, 'liab': liab})

# helpers

def dollars(s):
    return '$%s$' % (s,)

def mathrm(s, dollars=True):
    d = '$' if dollars else ''
    return r'%s\mathrm{%s}%s' % (d, r'\ '.join(s.split()), d)

def titles(t, *s): # title, hacky subtitles
    if not s:
        s = [commission_string]
    s = ['${}_{%s}$' % (x,) for x in s]
    return gg.ggtitle('\n'.join(['$%s$' % (t,)] + s))

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

    # We want these plots to continue to the top and left.
    return [ gg.coord_cartesian(xlim=x, ylim=y),
             gg.scale_x_continuous(limits=(x0, None), breaks=xbreaks),
             gg.scale_y_continuous(limits=(y0, None), breaks=ybreaks) ]
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
    print(basename)
    plot.save(savepath('%s.small.png' % (basename,)),
              width=2.4, height=1.8)
    print('%s - small' % (basename,))

def my_plot(df, x, y, color=None, clab=None):
    aes = { 'color': color, 'group': color } if color else {}
    if clab is None and color is not None:
        clab = color.replace('pr', "'")

    return (gg.ggplot(df, gg.aes(x, y, **aes))
            + labs(x, y)
            + (colors(clab) if color else []))

def main():
    mpl.rc('mathtext', fontset='cm')

    warnings.filterwarnings('ignore',
                            r'(geom|position)_\w+ ?: Removed \d+ rows')
    warnings.filterwarnings('ignore', r'Saving .+ x .+ in image')
    warnings.filterwarnings('ignore', r'Filename: .+\.png')

    df = concat_map(Pf_Ob_Ol, 'P_f', np.linspace(0.1, 1, 10))
    save_both(my_plot(df, 'O_b', 'O_l', 'P_f')
              + titles('P_f(O_b, O_l)')
              + limits((1, 10))
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              + gg.geom_line()
              , 'Pf_Ob_Ol')

    df = concat_map(Pf_Ob_σ, 'P_f', np.linspace(0.1, 1, 10))
    save_both(my_plot(df, 'O_b', 'σ', 'P_f')
              + titles('P_f(O_b, σ)')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Pf_Ob_σ')

    df = concat_map(Pq_Ob_Ol, 'P_q', np.linspace(-0.9, 0, 10))
    save_both(my_plot(df, 'O_b', 'O_l', 'P_q')
              + titles('P_q(O_b, O_l)')
              + limits((1, 10))
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              + gg.geom_line()
              , 'Pq_Ob_Ol')

    df = concat_map(Pq_Ob_σ, 'P_q', np.linspace(-0.9, 0, 10))
    save_both(my_plot(df, 'O_b', 'σ', 'P_q')
              + titles('P_q(O_b, σ)')
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Pq_Ob_σ')

    df = concat_map(Opr_Ob_Ol, 'Opr', np.linspace(1, 5, 9))
    save_both(my_plot(df, 'O_b', 'O_l', 'Opr')
              + titles("O'(O_b, O_l)")
              + limits((1, 10), (1, 10))
              + gg.geom_line()
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              , 'Opr_Ob_Ol')

    df = concat_map(Opr_Ob_σ, 'Opr', np.linspace(1, 5, 9))
    save_both(my_plot(df, 'O_b', 'σ', 'Opr')
              + titles("O'(O_b, σ)")
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'Opr_Ob_σ')

    df = (pd.DataFrame({'Opr': np.linspace(1, 21, 101)})
            .assign(Pf=lambda x: Opr_Pf(x.Opr)))
    save_both(my_plot(df, 'Opr', 'Pf')
              + titles("P_f(O')")
              + labs("O'", 'P_f')
              + limits((1, 20), (0, 1),
                       xbreaks=np.linspace(2, 20, 10),
                       ybreaks=np.linspace(0, 1, 11))
              + gg.geom_line()
              + gg.geom_hline(yintercept=C, linetype='dashed', color='grey')
              , 'Pf_Opr')

    df = concat_map(σpr_Ob_σ, 'σpr', np.linspace(0, 5, 11))
    save_both(my_plot(df, 'O_b', 'σ', 'σpr')
              + titles("σ'(O_b, σ)")
              + limits((1, 10), (0, 5))
              + gg.geom_line()
              , 'σpr_Ob_σ')

    df = (pd.DataFrame({'σpr': np.linspace(0, 21, 106)})
            .assign(Pq=lambda x: σpr_Pq(x.σpr)))
    save_both(my_plot(df, 'σpr', 'Pq')
              + titles("P_q(σ')")
              + labs("σ'", 'P_q')
              + limits((0, 20), (-1, 0),
                       xbreaks=np.linspace(0, 20, 11),
                       ybreaks=np.linspace(-1, 0, 11))
              + gg.geom_line()
              , 'Pq_σpr')

    df = concat_map(liab_Ob_Ol_free, 'liab', np.linspace(0, 10, 11))
    save_both(my_plot(df, 'O_b', 'O_l', 'liab', clab='-R_{bl}')
              + titles("-R_{bl}(O_b, O_l)", "S_b = 1, C_b = 0, C_l = 0.02",
                       mathrm('Free bet', dollars=False))
              + limits((1,20), (1, 10))
              + gg.geom_line()
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              , 'liab_Ob_Ol_free')

    df = concat_map(liab_Ob_Ol_free, 'liab', np.linspace(0, 10, 11))
    save_both(my_plot(df, 'O_b', 'σ', 'liab', clab='-R_{bl}')
              + titles("-R_{bl}(O_b, σ)", "S_b = 1, C_b = 0, C_l = 0.02",
                       mathrm('Free bet', dollars=False))
              + limits((1,20), (1, 10))
              + gg.geom_line()
              , 'liab_Ob_σ_free')

    df = concat_map(liab_Ob_Ol_qual, 'liab', np.linspace(0, 10, 11))
    save_both(my_plot(df, 'O_b', 'O_l', 'liab', clab='-R_{bl}')
              + titles("-R_{bl}(O_b, O_l)", "S_b = 1, C_b = 0, C_l = 0.02",
                       mathrm('Qualifying bet', dollars=False))
              + limits((1,20), (1, 10))
              + gg.geom_line()
              + gg.geom_abline(slope=1, intercept=0,
                               linetype='dashed', color='grey')
              , 'liab_Ob_Ol_qual')

    df = concat_map(liab_Ob_Ol_qual, 'liab', np.linspace(0, 10, 11))
    save_both(my_plot(df, 'O_b', 'σ', 'liab', clab='-R_{bl}')
              + titles("-R_{bl}(O_b, σ)", "S_b = 1, C_b = 0, C_l = 0.02",
                       mathrm('Qualifying bet', dollars=False))
              + limits((1,20), (1, 10))
              + gg.geom_line()
              , 'liab_Ob_σ_qual')

    df_Pf = Pf_Ob_σ(0.6).assign(profit=dollars('P_f'))
    df_Pq = Pq_Ob_σ(-0.3).assign(profit=dollars('P_q'))
    df = pd.concat((df_Pf, df_Pq), ignore_index=True)
    df.drop_duplicates('O_b', inplace=True)

    Opr = df_Pf.query('σ==0').O_b[0]
    σpr = df_Pq.query('O_b==1').σ[0]

    labels = pd.DataFrame({
        'x': [Opr+0.1, 1, 9.8], 'y': [4.8, σpr, σpr + 0.3],
        'label': ["$O'$", "$σ'$", mathrm('More profit')]
    })
    lab_aes = gg.aes('x', 'y', label='label')

    save_both(
        gg.ggplot(df, gg.aes(x='O_b', y='σ'))
        + gg.geom_area(gg.aes(fill='profit'), alpha=0.3)
        + gg.geom_vline(xintercept=Opr, linetype='dashed')
        + gg.geom_hline(yintercept=σpr, linetype='dashed')

        # text alignment can't be specified in an aes
        + gg.geom_text(lab_aes, data=labels.ix[:0], ha='left', va='top')
        + gg.geom_text(lab_aes, data=labels.ix[1:1], ha='left', va='bottom')
        + gg.geom_text(lab_aes, data=labels.ix[2:], ha='right', va='bottom')

        + gg.scale_fill_discrete(name=mathrm('Bet type'),
                                 labels=[mathrm('Free'), mathrm('Qualifying')])
        + limits((1, 10), (0, 5))
        + gg.ggtitle('%s "%s" %s' % (mathrm('Shape of the'),
                                     mathrm('more profitable'),
                                     mathrm('space')))
        + labs('O_b', 'σ')
        , 'Px_shapes')

if __name__ == '__main__':
    main()
