"""
Given a path to the GUM ../dep/ directory, extract each document's human-written summary and full text (untokenized),
and write to a .JSON file in the ../data/ directory of this repository.
"""


import os
import io
import json
import argparse
from collections import defaultdict


args = argparse.ArgumentParser()
args.add_argument("conllu_dir", type=str, help="path to directory where .conllu files are stored")
opts = args.parse_args()

conllu_dir = opts.conllu_dir


GUMSum_dict = defaultdict(lambda: defaultdict(str))  # only contain each document's full text and human1 summary
for file in os.listdir(conllu_dir):
	if file.endswith(".conllu") and file.startswith("GUM"):
		filename = file.split(".")[0]
		lines = io.open(os.path.join(conllu_dir, file), "r", encoding="utf-8").read().strip().split("\n")
		text_lines = []
		sum_line = ""
		for line in lines:
			if "# meta::summary = " in line:
				sum_line = line.split("# meta::summary = ")[1]
			elif line.startswith("# text = "):
				text_line = line.split("# text = ")[1]
				text_lines.append(text_line)
		text_string = " ".join(text_lines)

		GUMSum_dict[filename]["fulltext"] = text_string
		GUMSum_dict[filename]["human1"] = sum_line

assert len(GUMSum_dict) == len(os.listdir(conllu_dir))
GUMSum_dict_sorted = dict(sorted(GUMSum_dict.items(), key=lambda item: item[0]))  # sorted by genre and then docname

# write to .json
out_dir = os.path.dirname(os.path.abspath(__file__)).replace("utils", "data")
with open(os.path.join(out_dir, "GUMSum_human1.json"), "w") as f_out:
	json.dump(GUMSum_dict_sorted, f_out)
