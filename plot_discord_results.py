import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import os
import numpy as np

"""
Necessary inputs are a two text files from the concord discord processing
1) paired blood-saliva samples
2) blood and saliva replicates

This script producess venn diagrams from two VA subjects for, 6 venn diagrams per subject
1) Blood-Blood: ALL, SNP, INDEL
2) Saliva-Saliva: ALL, SNP, INDEL
3) Blood-Saliva: ALL, SNP, INDEL

This script also produces bar plots for concordance values for Blood-Saliva, Blood-Blood, Saliva-Saliva

See example outputs in 'plots_concordance'
"""
font = {'size': 20}
plt.rc('font', **font)

bs = pd.read_csv('concord_discord_filter_out/concord_discord_results.txt', sep='\t')
rep = pd.read_csv('concord_discord_filter_out/concord_discord_replicates_results.txt', sep='\t')


plotdir = 'plots_concordance/'
try:
    os.stat(plotdir)
except:
    os.mkdir(plotdir)

## make venn diagrams bs, bb, ss p1 and p2
##p1
s12_bs_p1 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s1_bs_p1 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s2_bs_p1 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()

s12_bb_p1 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s1_bb_p1 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s2_bb_p1 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()

s12_ss_p1 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s1_ss_p1 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s2_ss_p1 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()

s12_bs_p1_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s1_bs_p1_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s2_bs_p1_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()

s12_bb_p1_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s1_bb_p1_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s2_bb_p1_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()

s12_ss_p1_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s1_ss_p1_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s2_ss_p1_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()

s12_bs_p1_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s1_bs_p1_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()
s2_bs_p1_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_001_IonXpress_011')].item()

s12_bb_p1_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s1_bb_p1_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()
s2_bb_p1_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_035_IonXpress_001')].item()

s12_ss_p1_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s1_ss_p1_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()
s2_ss_p1_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_037_IonXpress_011')].item()

##p2
s12_bs_p2 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s1_bs_p2 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s2_bs_p2 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()

s12_bb_p2 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s1_bb_p2 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s2_bb_p2 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()

s12_ss_p2 = rep['s1ands2'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s1_ss_p2 = rep['s1only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s2_ss_p2 = rep['s2only'][(rep['type'] == 'all') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()

s12_bs_p2_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s1_bs_p2_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s2_bs_p2_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()

s12_bb_p2_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s1_bb_p2_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s2_bb_p2_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()

s12_ss_p2_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s1_ss_p2_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s2_ss_p2_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()

s12_bs_p2_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s1_bs_p2_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()
s2_bs_p2_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_002_IonXpress_012')].item()

s12_bb_p2_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s1_bb_p2_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()
s2_bb_p2_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_036_IonXpress_002')].item()

s12_ss_p2_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s1_ss_p2_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()
s2_ss_p2_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['sample'] == 'IonXpress_040_IonXpress_012')].item()

# all
plt.figure()
values = [s1_bs_p1, s2_bs_p1, s12_bs_p1]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p1_all.png')

plt.figure()
values = [s1_bb_p1, s2_bb_p1, s12_bb_p1]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p1_all.png')

plt.figure()
values = [s1_ss_p1, s2_ss_p1, s12_ss_p1]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p1_all.png')

plt.figure()
values = [s1_bs_p2, s2_bs_p2, s12_bs_p2]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p2_all.png')

plt.figure()
values = [s1_bb_p2, s2_bb_p2, s12_bb_p2]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p2_all.png')

plt.figure()
values = [s1_ss_p2, s2_ss_p2, s12_ss_p2]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p2_all.png')

# snp
plt.figure()
values = [s1_bs_p1_snp, s2_bs_p1_snp, s12_bs_p1_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p1_snp.png')

plt.figure()
values = [s1_bb_p1_snp, s2_bb_p1_snp, s12_bb_p1_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p1_snp.png')

plt.figure()
values = [s1_ss_p1_snp, s2_ss_p1_snp, s12_ss_p1_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p1_snp.png')

plt.figure()
values = [s1_bs_p2_snp, s2_bs_p2_snp, s12_bs_p2_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p2_snp.png')

plt.figure()
values = [s1_bb_p2_snp, s2_bb_p2_snp, s12_bb_p2_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p2_snp.png')

plt.figure()
values = [s1_ss_p2_snp, s2_ss_p2_snp, s12_ss_p2_snp]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p2_snp.png')

# indel
plt.figure()
values = [s1_bs_p1_indel, s2_bs_p1_indel, s12_bs_p1_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p1_indel.png')

plt.figure()
values = [s1_bb_p1_indel, s2_bb_p1_indel, s12_bb_p1_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p1_indel.png')

plt.figure()
values = [s1_ss_p1_indel, s2_ss_p1_indel, s12_ss_p1_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06224')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p1_indel.png')

plt.figure()
values = [s1_bs_p2_indel, s2_bs_p2_indel, s12_bs_p2_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Saliva']
# plt.title('Blood-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bs_p2_indel.png')

plt.figure()
values = [s1_bb_p2_indel, s2_bb_p2_indel, s12_bb_p2_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Blood            ', '     Blood repeat']
# plt.title('Blood-Blood % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_bb_p2_indel.png')

plt.figure()
values = [s1_ss_p2_indel, s2_ss_p2_indel, s12_ss_p2_indel]
values = [round(100 * float(v) / sum(values), 1) for v in values]
labels = ['Saliva           ', '     Saliva repeat']
# plt.title('Saliva-Saliva % Similarity 18-CG-15-06225')
venn2(subsets=values, set_labels=labels)
plt.savefig(plotdir + 'venn_ss_p2_indel.png')


## run these manually
# os.system('convert +append venn_bs_p1.png venn_bb_p1.png venn_ss_p1.png venn_p1.png')
# os.system('convert +append venn_bs_p2.png venn_bb_p2.png venn_ss_p2.png venn_p2.png')

def barplot(name, y_axis_title, all_list, snp_list, indel_list):
    font = {'size': 15}
    plt.rc('font', **font)

    fig, ax = plt.subplots()
    boxplot_data = [100 * all_list, 100 * snp_list, 100 * indel_list]
    box = ax.boxplot(boxplot_data, patch_artist=True)
    colors = ['red', 'blue', 'green']
    plt.setp(box['medians'], color='black')
    plt.setp(box['whiskers'], color='black')
    plt.setp(box['fliers'], color='white')

    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    for i, d in enumerate(boxplot_data):
        y = d
        x = np.random.normal(i + 1, 0.04, size=len(y))
        ax.plot(x, y, color='k', marker='.', linestyle='None', alpha=0.8)

    pmax = 100 * max(all_list)
    pmin = 100 * min(all_list)

    #   ax.text(1.5,pmax,round(ttest_ind(all_list,snp_list)[1],2))
    #   ax.text(2.5,pmax,round(ttest_ind(snp_list,indel_list)[1],2))
    #   ax.text(2,pmax,round(ttest_ind(all_list,indel_list)[1],2))

    #    ax.text(1.5,.95,round(mannwhitneyu(all_list,snp_list)[1],2))
    #    ax.text(2.5,.95,round(mannwhitneyu(snp_list,indel_list)[1],2))
    #    ax.text(2,.96,round(mannwhitneyu(all_list,indel_list)[1],2))

    #   plt.hlines(max(all_list),1,3)
    #   plt.hlines(max(all_list),1.3,1.8)
    #   plt.hlines(max(all_list),2.3,2.8)

    if (pmax > 90):
        plt.ylim(90, 98)
    else:
        plt.ylim(57, 72)

    ax.set_title(y_axis_title)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', linewidth=0.75)
    ax.set_axisbelow(True)
    plt.setp(ax, xticks=[1, 2, 3], xticklabels=['Blood-Saliva', 'Blood-Blood', 'Saliva-Saliva'])

    plt.savefig(plotdir + name + '.png')


## make boxplot for replicate runs
## first all independent replicates

s12_bs_all = bs['s1ands2'][bs['type'] == 'all']
s1_bs_all = bs['s1only'][bs['type'] == 'all']
s2_bs_all = bs['s2only'][bs['type'] == 'all']
s12_bs_snp = bs['s1ands2'][bs['type'] == 'snp']
s1_bs_snp = bs['s1only'][bs['type'] == 'snp']
s2_bs_snp = bs['s2only'][bs['type'] == 'snp']
s12_bs_indel = bs['s1ands2'][bs['type'] == 'indel']
s1_bs_indel = bs['s1only'][bs['type'] == 'indel']
s2_bs_indel = bs['s2only'][bs['type'] == 'indel']

s1_or_s2_bs_all = s1_bs_all + s2_bs_all
conc_bs_all = s12_bs_all / (s12_bs_all + s1_or_s2_bs_all)
s1_or_s2_bs_snp = s1_bs_snp + s2_bs_snp
conc_bs_snp = s12_bs_snp / (s12_bs_snp + s1_or_s2_bs_snp)
s1_or_s2_bs_indel = s1_bs_indel + s2_bs_indel
conc_bs_indel = s12_bs_indel / (s12_bs_indel + s1_or_s2_bs_indel)

s12_bb_all = np.array([s12_bb_p1, s12_bb_p2], dtype='float64')
s1_bb_all = np.array([s1_bb_p1, s1_bb_p2], dtype='float64')
s2_bb_all = np.array([s2_bb_p1, s2_bb_p2], dtype='float64')
s1_or_s2_bb_all = s1_bb_all + s2_bb_all
conc_bb_all = s12_bb_all / (s12_bb_all + s1_or_s2_bb_all)

s12_ss_all = np.array([s12_ss_p1, s12_ss_p2], dtype='float64')
s1_ss_all = np.array([s1_ss_p1, s1_ss_p2], dtype='float64')
s2_ss_all = np.array([s2_ss_p1, s2_ss_p2], dtype='float64')
s1_or_s2_ss_all = s1_ss_all + s2_ss_all
conc_ss_all = s12_ss_all / (s12_ss_all + s1_or_s2_ss_all)

s12_bb_snp = np.array([s12_bb_p1_snp, s12_bb_p2_snp], dtype='float64')
s1_bb_snp = np.array([s1_bb_p1_snp, s1_bb_p2_snp], dtype='float64')
s2_bb_snp = np.array([s2_bb_p1_snp, s2_bb_p2_snp], dtype='float64')
s1_or_s2_bb_snp = s1_bb_snp + s2_bb_snp
conc_bb_snp = s12_bb_snp / (s12_bb_snp + s1_or_s2_bb_snp)

s12_ss_snp = np.array([s12_ss_p1_snp, s12_ss_p2_snp], dtype='float64')
s1_ss_snp = np.array([s1_ss_p1_snp, s1_ss_p2_snp], dtype='float64')
s2_ss_snp = np.array([s2_ss_p1_snp, s2_ss_p2_snp], dtype='float64')
s1_or_s2_ss_snp = s1_ss_snp + s2_ss_snp
conc_ss_snp = s12_ss_snp / (s12_ss_snp + s1_or_s2_ss_snp)

s12_bb_indel = np.array([s12_bb_p1_indel, s12_bb_p2_indel], dtype='float64')
s1_bb_indel = np.array([s1_bb_p1_indel, s1_bb_p2_indel], dtype='float64')
s2_bb_indel = np.array([s2_bb_p1_indel, s2_bb_p2_indel], dtype='float64')
s1_or_s2_bb_indel = s1_bb_indel + s2_bb_indel
conc_bb_indel = s12_bb_indel / (s12_bb_indel + s1_or_s2_bb_indel)

s12_ss_indel = np.array([s12_ss_p1_indel, s12_ss_p2_indel], dtype='float64')
s1_ss_indel = np.array([s1_ss_p1_indel, s1_ss_p2_indel], dtype='float64')
s2_ss_indel = np.array([s2_ss_p1_indel, s2_ss_p2_indel], dtype='float64')
s1_or_s2_ss_indel = s1_ss_indel + s2_ss_indel
conc_ss_indel = s12_ss_indel / (s12_ss_indel + s1_or_s2_ss_indel)

barplot('concordance_all_independent', '% Similarity (independent only)', conc_bs_all, conc_bb_all, conc_ss_all)
barplot('concordance_snp_independent', '% SNP Similarity (independent only)', conc_bs_snp, conc_bb_snp, conc_ss_snp)
barplot('concordance_indel_independent', '% Indel Similarity (independent only)', conc_bs_indel, conc_bb_indel,
        conc_ss_indel)

### then with all data from replicates only

# s12_bs = rep['s1ands2'][rep['type'] ==  'bloodsaliva']
# s1_bs = rep['s1only'][rep['type'] == 'bloodsaliva']
# s2_bs = rep['s2only'][rep['type'] == 'bloodsaliva']
# s1_or_s2_bs = s1_bs + s2_bs
# conc_bs = s12_bs/(s12_bs + s1_or_s2_bs)

s12_bb_all = rep['s1ands2'][(rep['type'] == 'all') & (rep['comparison'] == 'blood')]
s1_bb_all = rep['s1only'][(rep['type'] == 'all') & (rep['comparison'] == 'blood')]
s2_bb_all = rep['s2only'][(rep['type'] == 'all') & (rep['comparison'] == 'blood')]
s1_or_s2_bb_all = s1_bb_all + s2_bb_all
conc_bb_all = s12_bb_all / (s12_bb_all + s1_or_s2_bb_all)

s12_ss_all = rep['s1ands2'][(rep['type'] == 'all') & (rep['comparison'] == 'saliva')]
s1_ss_all = rep['s1only'][(rep['type'] == 'all') & (rep['comparison'] == 'saliva')]
s2_ss_all = rep['s2only'][(rep['type'] == 'all') & (rep['comparison'] == 'saliva')]
s1_or_s2_ss_all = s1_ss_all + s2_ss_all
conc_ss_all = s12_ss_all / (s12_ss_all + s1_or_s2_ss_all)
print conc_bs_all
print conc_bb_all
print conc_ss_all

barplot('concordance_all_reps', '% Similarity', conc_bs_all, conc_bb_all, conc_ss_all)

s12_bb_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['comparison'] == 'blood')]
s1_bb_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['comparison'] == 'blood')]
s2_bb_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['comparison'] == 'blood')]
s1_or_s2_bb_snp = s1_bb_snp + s2_bb_snp
conc_bb_snp = s12_bb_snp / (s12_bb_snp + s1_or_s2_bb_snp)

s12_ss_snp = rep['s1ands2'][(rep['type'] == 'snp') & (rep['comparison'] == 'saliva')]
s1_ss_snp = rep['s1only'][(rep['type'] == 'snp') & (rep['comparison'] == 'saliva')]
s2_ss_snp = rep['s2only'][(rep['type'] == 'snp') & (rep['comparison'] == 'saliva')]
s1_or_s2_ss_snp = s1_ss_snp + s2_ss_snp
conc_ss_snp = s12_ss_snp / (s12_ss_snp + s1_or_s2_ss_snp)

barplot('concordance_snp_reps', '% SNP Similarity', conc_bs_snp, conc_bb_snp, conc_ss_snp)

s12_bb_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['comparison'] == 'blood')]
s1_bb_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['comparison'] == 'blood')]
s2_bb_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['comparison'] == 'blood')]
s1_or_s2_bb_indel = s1_bb_indel + s2_bb_indel
conc_bb_indel = s12_bb_indel / (s12_bb_indel + s1_or_s2_bb_indel)

s12_ss_indel = rep['s1ands2'][(rep['type'] == 'indel') & (rep['comparison'] == 'saliva')]
s1_ss_indel = rep['s1only'][(rep['type'] == 'indel') & (rep['comparison'] == 'saliva')]
s2_ss_indel = rep['s2only'][(rep['type'] == 'indel') & (rep['comparison'] == 'saliva')]
s1_or_s2_ss_indel = s1_ss_indel + s2_ss_indel
conc_ss_indel = s12_ss_indel / (s12_ss_indel + s1_or_s2_ss_indel)

barplot('concordance_indel_reps', '% Indel Similarity', conc_bs_indel, conc_bb_indel, conc_ss_indel)
