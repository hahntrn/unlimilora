def parse(result, experiment):
    latex = f"\\textbf{{{experiment}}}"
    for i,line in enumerate(result.split("\n")):
        # if i > 10 or (i > 2 and i < 6):
        #     continue
        if "/" not in line:
            continue
        line = line.split("=")
        metric = line[0].split("/")[1].strip()
        value = line[1].strip()
        latex += f" & {value}"
    return latex

def print_table(parsed):
    for table in parsed:
        print('\n'.join(parsed[table]))

def main():
    datasets = ['gov_report']
    experiments = ['bert-base']
    results = {}
    for dataset in datasets:
        if dataset not in results:
            results[dataset] = {}
        for experiment in experiments:
            if experiment not in results[dataset]:
                results[dataset][experiment] = ""
    print(results)

    results['gov_report']['BART-base'] = """\
eval_bertscore/f1                      =     0.4291
eval_bertscore/precision               =     0.3822
eval_bertscore/recall                  =     0.4924
eval_mean_prediction_length_characters =  3166.0312
eval_mean_prediction_length_tokens     =   910.9219
eval_num_predicted                     =        128
eval_rouge/geometric_mean              =     5.5801
eval_rouge/rouge1                      =    14.0551
eval_rouge/rouge2                      =     1.7036
eval_rouge/rougeL                      =     7.2567
eval_rouge/rougeLsum                   =    13.0884
eval_runtime                           = 0:15:44.29
eval_samples                           =        128
eval_samples_per_second                =      0.136
eval_steps_per_second                  =      0.017"""

    results['gov_report']['BART finetuned'] = None

    results['gov_report']['BART finetuned w/ LoRA'] = None

    results['gov_report']['BART finetuned w/ int8 quantization'] = None

    results['gov_report']['BART finetuned w/ LoRA + int8 quantization'] = None

    import pdb; pdb.set_trace()
    first_line = '\\textbf{Metrics} & f1 & precision & recall & geometric mean & rouge1 & rouge2 & rougeL & rougeLsum \\\\ \\hline'
    parsed = {}
    for dataset in datasets:
        if dataset not in parsed:
            parsed[dataset] = []
        for experiment in experiments:
            parsed[dataset].append(parse(results[dataset][experiment], experiment))
    print_table(parsed)

main()