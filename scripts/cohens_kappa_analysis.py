import pandas as pd
from sklearn.metrics import cohen_kappa_score
from itertools import combinations

FILE_PATH = "intensifiers.csv"
df = pd.read_csv(FILE_PATH)

GEMINI_COLS = [
    "Gemini_Zero-shot (formal)", "Gemini_Few-shot (formal)",
    "Gemini_Zero-shot (friendly)", "Gemini_Few-shot (friendly)"
]
GPT_COLS = [
    "GPTo4-mini_Zero-shot (formal)", "GPTo4-mini_Few-shot (formal)",
    "GPTo4-mini_Zero-shot (friendly)", "GPTo4-mini_Few-shot (friendly)"
]
DEEPSEEK_COLS = [
    "DeepSeek_Zero-shot (formal)", "DeepSeek_Few-shot (formal)",
    "DeepSeek_Zero-shot (friendly)", "DeepSeek_Few-shot (friendly)"
]
ALL_COLS = GEMINI_COLS + GPT_COLS + DEEPSEEK_COLS

# Build presence/absence matrix
all_intensifiers = sorted(set(
    v for col in ALL_COLS if col in df.columns
    for v in df[col].dropna().str.strip().str.lower()
))
matrix = pd.DataFrame(index=all_intensifiers, columns=ALL_COLS, data=0)
for col in ALL_COLS:
    if col in df.columns:
        for v in df[col].dropna().str.strip().str.lower():
            matrix.loc[v, col] = 1

# Aggregate to model level
matrix["Gemini"]     = matrix[GEMINI_COLS].max(axis=1)
matrix["GPT4o_mini"] = matrix[GPT_COLS].max(axis=1)
matrix["DeepSeek"]   = matrix[DEEPSEEK_COLS].max(axis=1)

# Condition-level vectors
def cond(cols): return matrix[[c for c in cols if c in matrix.columns]].max(axis=1)
matrix["formal"]   = cond([c for c in ALL_COLS if "formal"   in c.lower()])
matrix["friendly"] = cond([c for c in ALL_COLS if "friendly" in c.lower()])
matrix["zeroshot"] = cond([c for c in ALL_COLS if "zero"     in c.lower()])
matrix["fewshot"]  = cond([c for c in ALL_COLS if "few"      in c.lower()])

def interpret(k):
    if k < 0: return "Poor"
    elif k < 0.20: return "Slight"
    elif k < 0.40: return "Fair"
    elif k < 0.60: return "Moderate"
    elif k < 0.80: return "Substantial"
    else: return "Almost perfect"

# Compute kappa
rows = []
for m1, m2 in combinations(["Gemini", "GPT4o_mini", "DeepSeek"], 2):
    k = cohen_kappa_score(matrix[m1], matrix[m2])
    rows.append({"Comparison": f"{m1} vs {m2}", "Kappa": round(k, 3), "Interpretation": interpret(k)})

for label, c1, c2 in [("Formal vs Friendly", "formal", "friendly"), ("Zero-shot vs Few-shot", "zeroshot", "fewshot")]:
    k = cohen_kappa_score(matrix[c1], matrix[c2])
    rows.append({"Comparison": label, "Kappa": round(k, 3), "Interpretation": interpret(k)})

kappa_df = pd.DataFrame(rows)
print(kappa_df.to_string(index=False))
kappa_df.to_csv("kappa_results.csv", index=False)