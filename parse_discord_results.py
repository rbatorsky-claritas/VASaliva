__author__ = 'rebeccabatorsky'
import glob
import os
import subprocess

"""
Parse the concord discord files to produce a results text file for plotting.

Necessary input is a text file listing samples to compare and run metrics.
Samples are in order as the sample sheet, first 10 blood, second 10 saliva.

The directory where the output of the concord discord results needs to be provided.

"""
## read data
f = open("Saliva_VA_Project_orderfixed_duplicateanalysis_totalreads.txt",'r')
data_dir = '/Users/rebeccabatorsky/Claritas/comparator/VA_saliva/'
i=0
blood_vcf = []
saliva_vcf = []

blood_barcode = []
saliva_barcode = []

for line in f:
    i+=1
    arr = line.split("\t")
    index = arr[2]
    run = arr[3]
    vcf = glob.glob(data_dir + '*' + run + '*' + '/plugin_out/variantCaller_out*/' + index + '/TSVC_variants.vcf')
    if (i<11):
        blood_vcf.append(vcf)
        blood_barcode.append(index)
    else:
        saliva_vcf.append(vcf)
        saliva_barcode.append(index)

print len(blood_vcf)
print len(saliva_vcf)
outdir = "concord_discord_filter_out/"

f = open(outdir + 'concord_discord_results.txt','w')
f.write("sample\ttype\ts1\ts2\ts1ands2\ts1only\ts2only\n")
for i in xrange(0,10):
    bj = blood_vcf[i][0]
    sk = saliva_vcf[i][0]

    bj_barcode = blood_barcode[i]
    sk_barcode = saliva_barcode[i]

    #all
    arr = []
    arr.append(bj_barcode + "_" + sk_barcode)
    arr.append("all")
    arr.append(subprocess.check_output(["grep ^chr " + bj + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + sk + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir +  bj_barcode + "_and_" + sk_barcode + ".vcf | wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir +  bj_barcode + "_not_" + sk_barcode + ".vcf | wc -l" ],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir + sk_barcode + "_not_" + bj_barcode + ".vcf | wc -l" ],shell=True).rstrip())
    str = '\t'.join(arr).replace(" ","")
    f.write(str + '\n')

    #snp
    arr = []
    arr.append(bj_barcode + "_" + sk_barcode)
    arr.append("snp")
    arr.append(subprocess.check_output(["grep ^chr " + bj + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + sk + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir +  bj_barcode + "_and_" + sk_barcode + "_snp.vcf | wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir +  bj_barcode + "_not_" + sk_barcode + "_snp.vcf | wc -l" ],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir + sk_barcode + "_not_" + bj_barcode + "_snp.vcf | wc -l" ],shell=True).rstrip())
    str = '\t'.join(arr).replace(" ","")
    f.write(str + '\n')

    #indel
    arr = []
    arr.append(bj_barcode + "_" + sk_barcode)
    arr.append("indel")
    arr.append(subprocess.check_output(["grep ^chr " + bj + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + sk + "| wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir +  bj_barcode + "_and_" + sk_barcode + "_indel.vcf | wc -l"],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir +  outdir +  bj_barcode + "_not_" + sk_barcode + "_indel.vcf | wc -l" ],shell=True).rstrip())
    arr.append(subprocess.check_output(["grep ^chr " + data_dir + outdir + sk_barcode + "_not_" + bj_barcode + "_indel.vcf | wc -l" ],shell=True).rstrip())
    str = '\t'.join(arr).replace(" ","")
    f.write(str + '\n')

