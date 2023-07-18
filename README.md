# GUMSum4EVAL


### *Repository for ACL 2023 (Findings): [GUMSum: Multi-Genre Data and Evaluation for English Abstractive Summarization](https://aclanthology.org/2023.findings-acl.593/)*
```
@inproceedings{liu-zeldes-2023-gumsum,
    title = "{GUMS}um: Multi-Genre Data and Evaluation for {E}nglish Abstractive Summarization",
    author = "Liu, Yang Janet  and
      Zeldes, Amir",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.593",
    pages = "9315--9327",
    abstract = "Automatic summarization with pre-trained language models has led to impressively fluent results, but is prone to {`}hallucinations{'}, low performance on non-news genres, and outputs which are not exactly summaries. Targeting ACL 2023{'}s {`}Reality Check{'} theme, we present GUMSum, a small but carefully crafted dataset of English summaries in 12 written and spoken genres for evaluation of abstractive summarization. Summaries are highly constrained, focusing on substitutive potential, factuality, and faithfulness. We present guidelines and evaluate human agreement as well as subjective judgments on recent system outputs, comparing general-domain untuned approaches, a fine-tuned one, and a prompt-based approach, to human performance. Results show that while GPT3 achieves impressive scores, it still underperforms humans, with varying quality across genres. Human judgments reveal different types of errors in supervised, prompted, and human-generated summaries, shedding light on the challenges of producing a good summary.",
}
```

## OBTAIN THE DATA
The underlying `full texts` for the `reddit` data (`document id` in the form of `GUM_reddit_*`) are currently ❗**underscored**❗
due to data license issues. The existing `.json` file under `../data/` named `GUMSum_underscored.json` do not contain 
full texts of all the reddit documents. 

In order to reconstruct the underlying texts, follow the steps below to run `python get_reddit_text.py`, and when prompted, 
please confirm that you are solely responsible for downloading reddit data and may only use it for non-commercial purposes. 

```
git clone https://github.com/janetlauyeung/GUMSum4EVAL.git
cd GUMSum4EVAL/utils/
python get_reddit_text.py
```

Then you should be able to see a new `.json` file called `GUMSum_final.json` under `../data/`. You can read and load the 
`.json file` into a nested dictionary by doing the following:
```
import os
import io
import json

gumsum_dict = json.load(io.open(os.path.join(data_dir, "GUMSum_final.json")))
```
At a minimum, each document id corresponds to two key-value pairs: 
- `gumsum_dict[DOCID]["fulltext"]`: the untokenized full text of the given document
- `gumsum_dict[DOCID]["human1"]`: a human-written summary for the given document

The entire GUMSum (i.e. 213 documents) is intended to be a test set for summarization generalization across genres. 
We used the 24 document subset for the human evaluation, and this portion was double annotated (as described in the [paper](https://arxiv.org/abs/2306.11256)) 
by collecting a second human-written summary as well as the system-generated summaries from 2 supervised systems, GPT3, and a fine-funing BRIO using GUMSum:
- `gumsum_dict[DOCID]["human2"]`: a second human-written summary for the given document
- `gumsum_dict[DOCID]["brio"]`: a system-generated summary using [the BRIO model (Liu et al., ACL 2022)](https://aclanthology.org/2022.acl-long.207/)
- `gumsum_dict[DOCID]["simcls"]`: a system-generated summary using [the SimCLS model (Liu & Liu, ACL-IJCNLP 2021)](https://aclanthology.org/2021.acl-short.135/)
- `gumsum_dict[DOCID]["gpt3"]`: a system-generated summary using `GPT3-text-davinci-002`
- `gumsum_dict[DOCID]["brioft"]`: a system-generated summary by fine-tuning the BRIO model using GUMSum




## HUMAN EVALUATION 
We conducted a human evaluation and asked participants (12 Linguistics students) to write a summary following the guidelines 
and answer questions focusing on the following aspects and provide justifications when applicable. 
Please see the appendices of the paper for a full copy of the survey.
1. preference 
2. substitutive
3. hallucination 
4. faithfulness 
5. english quality
6. source
7. difficulty

We also make these responses available for interested researchers in order to facilitate discussions 
on what's considered a good summary and what are the challenges and difficulties. 
You can access the responses of our human evaluation [here](https://docs.google.com/spreadsheets/d/e/2PACX-1vQlwJgTH115Bi_CRCfZQnmVD7hkHz4jnwPwVYq_mn7tINMgLFKM5COvh4ktxLsujb4JDRiDpUvt3qib/pubhtml). 
If you'd like to obtain a copy of these responses, please reach out! 
