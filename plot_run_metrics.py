__author__ = 'rebeccabatorsky'
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_rel
import os

"""
Necessary input is a text file listing samples to compare and run metrics.
Samples are in order as the sample sheet, first 10 blood, second 10 saliva.

This script produces a plot for each run metric, with two subplots
First shows a subject-by-subject bar plot
Second shows a group comparison between blood and saliva groups

See example outputs in 'plots_runmetrics'
"""


def read_input_file():
    f = open("Saliva_VA_Project_orderfixed_duplicateanalysis_totalreads.txt", 'r')

    i = 0
    for line in f:
        i += 1
        arr = line.split("\t")
        index = arr[2]
        run = arr[3]

        if (i < 11):
            blood_barcode.append(index)
            blood_ontarget.append(float(arr[4]))
            blood_meantarget.append(float(arr[5]))
            blood_uniformity.append(float(arr[6]))
            blood_20x.append(float(arr[7]))
            blood_meanread.append(int(arr[8]))
            blood_totalread.append(int(arr[9]))


        else:
            saliva_barcode.append(index)
            saliva_ontarget.append(float(arr[4]))
            saliva_meantarget.append(float(arr[5]))
            saliva_uniformity.append(float(arr[6]))
            saliva_20x.append(float(arr[7]))
            saliva_meanread.append(int(arr[8]))
            saliva_totalread.append(int(arr[9]))


def sort_and_plot(name, title, y_axis_title, blood_list, saliva_list):
    font = {'size': 15}

    plt.rc('font', **font)

    ind = np.arange(len(blood_list))
    width = float(0.4)
    second = ind + width
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    boxplot_data = [blood_list, saliva_list]
    box = ax[1].boxplot(boxplot_data, patch_artist=True, showmeans=True, meanline=True)
    colors = ['red', 'blue']
    plt.setp(box['means'], color='black')
    plt.setp(box['medians'], color='black')
    t, p = ttest_rel(blood_list, saliva_list)

    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    for i, d in enumerate(boxplot_data):
        y = d
        x = np.random.normal(i + 1, 0.04, size=len(y))
        ax[1].plot(x, y, color='k', marker='.', linestyle='None', alpha=0.8)

    ax[1].set_title(title)
    ax[1].yaxis.grid(True, linestyle='-', which='major', color='lightgrey', linewidth=0.75)
    ax[1].set_axisbelow(True)
    plt.setp(ax, xticks=[1, 2], xticklabels=['Blood', 'Saliva'''])

    if (p < 0.05):
        ax[1].text(1.3, np.mean(blood_list), 'p = %.0e' % p)
    else:
        ax[1].text(1.3, np.mean(blood_list), 'p = ' + str(round(p, 2)))

    ax[0].bar(ind, blood_list, width, color='red', label='blood')
    ax[0].bar(second, saliva_list, width, color='blue', label='saliva')
    ax[0].set(xticks=ind + width, xticklabels=xrange(1, len(blood_list) + 1), xlim=[2 * width - 1, len(blood_list)])
    ax[0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    ax[0].set_ylabel(y_axis_title)
    ax[0].set_xlabel('Subject number')
    plt.savefig(plotdir + name + '.png')


### fill lists of values to plot
blood_barcode = []
blood_ontarget = []
blood_meantarget = []
blood_uniformity = []
blood_20x = []
blood_meanread = []
blood_totalread = []

saliva_barcode = []
saliva_ontarget = []
saliva_meantarget = []
saliva_uniformity = []
saliva_20x = []
saliva_meanread = []
saliva_totalread = []
read_input_file()

read_input_file()
plotdir = 'plots_runmetrics/'
try:
    os.stat(plotdir)
except:
    os.mkdir(plotdir)

sort_and_plot('on_target', '', 'On Target Reads (%)', blood_ontarget, saliva_ontarget)
sort_and_plot('mean_target_cov', '', 'Mean Target Coverage (reads)', blood_meantarget, saliva_meantarget)
sort_and_plot('uniformity', '', 'Uniformity (%)', blood_uniformity, saliva_uniformity)
sort_and_plot('20x', '', '20X Coverage (%)', blood_20x, saliva_20x)
sort_and_plot('mean_read', '', 'Mean Read length (bp)', blood_meanread, saliva_meanread)
sort_and_plot('total_read', '', 'Total Mapped Reads', blood_totalread, saliva_totalread)
