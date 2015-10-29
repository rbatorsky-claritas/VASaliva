import glob
import os

"""
Run select_variants_discord_vasaliva.sh on a set of samples

Necessary input is a text file listing samples to compare and run metrics.
Samples are in order as the sample sheet, first 10 blood, second 10 saliva.

"""

def processVcf(vcffile1, vcffile2, barcode1, barcode2, outdir):
    command = './select_variants_discord_vasaliva.sh ' + vcffile1 + ' ' + vcffile2 + ' ' + barcode1 + ' ' + barcode2 + ' ' + outdir
    os.system(command)


def read_input_file():
    f = open("Saliva_VA_Project_orderfixed_duplicateanalysis_totalreads.txt", 'r')
    data_dir = "/Users/rebeccabatorsky/Claritas/comparator/VA_saliva/"
    i = 0
    blood_vcf = []
    saliva_vcf = []

    blood_barcode = []
    saliva_barcode = []

    for line in f:
        i += 1
        arr = line.split("\t")
        index = arr[2]
        run = arr[3]
        vcf = glob.glob(
            data_dir + 'Auto_user*' + run + '*' + '/plugin_out/variantCaller_out*/' + index + '/TSVC_variants.vcf')
        if (i < 11):
            blood_vcf.append(vcf)
            blood_barcode.append(index)
        else:
            saliva_vcf.append(vcf)
            saliva_barcode.append(index)
    return blood_vcf, blood_barcode, saliva_vcf, saliva_barcode


blood_vcf, blood_barcode, saliva_vcf, saliva_barcode = read_input_file()
print len(blood_vcf)
print len(saliva_vcf)

if len(blood_vcf) != len(saliva_vcf):
    print "Error blood and saliva lists are not the same length! Check input file."
    exit()

outdir = "concord_discord_filter_out"

for i in xrange(0, 11):
    bj = blood_vcf[i][0]
    sk = saliva_vcf[i][0]

    bj_barcode = blood_barcode[i]
    sk_barcode = saliva_barcode[i]

    processVcf(bj, sk, bj_barcode, sk_barcode, outdir)
