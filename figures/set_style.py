import matplotlib.pyplot as plt

def set_style(style='article', w=1, h=1):
   sdict = {
       'article': {
           # (11pt font = 360pt, 4.98) (10pt font = 345pt, 4.77)
           'figure.figsize' : (4.98 * w, 2 * h),
           'lines.linewidth': 1,
           'lines.markersize': 1.5,
           'font.size'      : 11,
           'legend.frameon' : False,
           #'legend.fontsize': 8,
           'font.family'    : 'serif',
           'text.usetex'    : True,
           'xtick.direction': 'in',
           'ytick.direction': 'in'
       }}
#       'notebook': {
#           'figure.figsize' : (16, 9),
#           'axes.labelsize' : 50,
#           'lines.linewidth': 4,
#           'lines.markersize': 20,
#           'xtick.labelsize': 40,
#           'ytick.labelsize': 50,
#           'axes.titlesize' : 20,
#           'font.size'      : 50,
#           'legend.frameon' : False,
#           'legend.fontsize': 35,
#           'font.family'    : 'serif',
#           'text.usetex'    : True
#       }
#   }
   rc = sdict[style]
   plt.rcParams.update(rc)
