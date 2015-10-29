10/29/15

These are the basic analysis scripts used to produce the presentation for the VA 

https://docs.google.com/a/claritasgenomics.com/presentation/d/1eXlF2Are1rQjdnq4MucG_Dm0Uinn15v7_OCiRUI7lVg/edit?usp=sharing

The main input file on git has been censored: Saliva_VA_Project_orderfixed_duplicateanalysis_totalreads.txt
It is copied from the sample sheet. It lists, in order, the 10 blood samples followed by the 10 saliva samples, followed by the run metrics.
Run metric order is: percent on target, mean target coverage, uniformity, coverage at 20X, mean read lenth, number of mapped reads


1) plot_run_metric.py
Produces plots of run metrics as listed on sample sheet.
Each plot has two subplots:
First shows a subject-by-subject bar plot
Second shows a group comparison between blood and saliva groups

2) run_select_variants_discord_va_saliva_cluster.py
Runs GATK select variants concordance and discordance method on blood-saliva samples (10) as well as blood-blood and saliva-saliva replicates (2 subjects, 3 reps each)

2) parse_discord_results.py
Parses the results of the concord and discord analysis into files concord_discord_results.txt

3) plot_discord_results.py
Produces both Venn diagrams and bar plots of the concordance and discordance results.
Producess venn diagrams from two VA subjects for, 6 venn diagrams per subject
- Blood-Blood: ALL, SNP, INDEL
- Saliva-Saliva: ALL, SNP, INDEL
- Blood-Saliva: ALL, SNP, INDEL

