"""Narrow deterministic replay of the frozen pricing fixture, not a model run.
Recognizes only the exact saved current-price sentence pattern; unfamiliar applicable
wording returns REVIEW, never silently passes. Unrelated rows are not evaluated.
"""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'evidence/ascend-iq-20-cases.csv').open()))
results=[]
for r in rows:
    if r['question']!="What is InsightFlow's pricing for Enterprise?":
        results.append({'row':int(r['row']),'status':'NOT_APPLICABLE'});continue
    current=re.search(r'New Price \(Updated yesterday\): \$(\d+(?:\.\d+)?)',r['reference'])
    quoted=re.search(r'Enterprise starts at \$(\d+(?:\.\d+)?)',r['answer'])
    status='REVIEW' if not(current and quoted) else ('PASS' if current.group(1)==quoted.group(1) else 'FAIL')
    results.append({'row':int(r['row']),'status':status,'quoted':quoted.group(1) if quoted else None,'reference_current':current.group(1) if current else None})
report={'scope':'Frozen numeric-price fixture only; no semantic-judge or agent execution','applicable':sum(r['status']!='NOT_APPLICABLE' for r in results),'failed':sum(r['status']=='FAIL' for r in results),'results':results}
(root/'evidence/pricing-replay.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
