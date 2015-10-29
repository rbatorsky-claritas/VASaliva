#!/bin/bash

numofargs=$#
if [ $numofargs -eq 5 ]; then
        vcf1=$1
	vcf2=$2
	sample_id1=$3
	sample_id2=$4
	vcf_dir=$5

        if [[ $vcf1 == *\.vcf ]]; then
		echo "Starting"
        else
                echo "Input vcf file must be vcf1.vcf vcf2.vcf outdir"
								echo $vcf1
                exit 1
        fi
else
        echo "Input vcf file must be vcf1.vcf vcf2.vcf outdir"
        exit 1
fi

vcf1_path=$vcf1
vcf2_path=$vcf2

mkdir -p $vcf_dir 

#sample_id1=$(bcftools query -l $vcf1_path)
#sample_id2=$(bcftools query -l $vcf2_path)

gatk_path=~/BioSoftware/GenomeAnalysisTK-3.3-0/GenomeAnalysisTK.jar
hg19_path=/workflow-deployment/configuration/genome-assemblies/hg19.fasta 

java -Xmx2g -jar $gatk_path \
	-R $hg19_path \
	-T SelectVariants \
	--variant $vcf1_path \
	--discordance	$vcf2_path \
	-o ${vcf_dir}/${sample_id1}_not_${sample_id2}.vcf

java -Xmx2g -jar $gatk_path \
	-R $hg19_path \
	-T SelectVariants \
	--variant $vcf2_path \
	--discordance	$vcf1_path \
	-o ${vcf_dir}/${sample_id2}_not_${sample_id1}.vcf

java -Xmx2g -jar $gatk_path \
	-R $hg19_path \
	-T SelectVariants \
	--variant $vcf1_path \
	--concordance	$vcf2_path \
	-o ${vcf_dir}/${sample_id1}_and_${sample_id2}.vcf





