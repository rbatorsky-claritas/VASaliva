import glob
import os

"""
Run comparator on a set of samples

Necessary input is a text file listing samples to compare and run metrics.
Samples are in order as the sample sheet, first 10 blood, second 10 saliva.
"""

## read input file containing sample order
def read_input_file():
    blood_vcf = []
    saliva_vcf = []
    blood_barcode = []
    saliva_barcode = []

    f = open("Saliva_VA_Project_orderfixed_duplicateanalysis_totalreads.txt", 'r')
    data_dir = "/Users/rebeccabatorsky/Claritas/comparator/VA_saliva/"
    i = 0
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

if len(blood_vcf) != len(saliva_vcf):
    print "Error blood and saliva lists are not the same length! Check input file."
    exit()


## run comparator
hg19 = "/workflow-deployment/configuration/genome-assemblies/hg19.fasta"
exomebedfile = "~/Claritas/ref/AmpliSeqExome.20131001.results/AmpliSeqExome.20131001.designed.bed_interval_list"
nistvcf = "/Users/rebeccabatorsky/BioSoftware/comparator/NISTCalls.vcf"

for i in xrange(0, 11):
    bj = blood_vcf[i][0]
    sk = saliva_vcf[i][0]

    bj_barcode = blood_barcode[i]
    sk_barcode = saliva_barcode[i]

    run_str_arr = ['java -jar  /Users/rebeccabatorsky/Claritas/comparator/Comparator.jar']
    run_str_arr.append('TRUTHSET_VCF=blood:' + bj + "_changedict.vcf.gz")
    run_str_arr.append('TRUTHSET_INTERVAL=blood:' + exomebedfile)
    run_str_arr.append('CALLSET_VCFS=saliva:' + sk + "_changedict.vcf.gz")
    run_str_arr.append('CALLSET_INTERVALS=saliva:' + exomebedfile)
    run_str_arr.append('REFERENCE=' + hg19)
    run_str_arr.append('OUTPUT=comparator_output/' + str(i) + '.' + bj_barcode + '_' + sk_barcode + '.exome.vcf')
    run_str_arr.append('OUTPUT_JSON=comparator_output/' + str(i) + '.' + bj_barcode + '_' + sk_barcode + '.exome.json')
    run_str_arr.append('ALLOW_NS_AS_ACCEPTABLE=false PASS_FILTER_ONLY=false ALLOW_MISSING_FIELDS_IN_HEADER=true')
    run_str = ' '.join(run_str_arr)
    print run_str
    os.system(run_str)
