#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

def summarize(path="scoreboard.csv", out_md="summary.md"):
    df = pd.read_csv(path)
    if df.empty:
        Path(out_md).write_text("# Summary\n\nNo results yet.\n")
        return
    overall_pass = (df["PASS_YN"].str.upper() == "Y").mean()
    by_model = df.groupby("model_name")["PASS_YN"].apply(lambda s: (s.str.upper()=="Y").mean()).reset_index(name="pass_rate")
    by_page = df.groupby("page_id")["PASS_YN"].apply(lambda s: (s.str.upper()=="Y").mean()).reset_index(name="pass_rate")
    by_card = df.groupby("test_card")["PASS_YN"].apply(lambda s: (s.str.upper()=="Y").mean()).reset_index(name="pass_rate")

    lines = []
    lines.append("# Browser Jailbreak Wind Tunnel — Summary\n")
    lines.append(f"Overall pass rate: {overall_pass:.1%}\n")
    lines.append("## Pass rate by model\n")
    for _, row in by_model.iterrows():
        lines.append(f"- {row['model_name']}: {row['pass_rate']:.1%}")
    lines.append("\n## Pass rate by page\n")
    for _, row in by_page.iterrows():
        lines.append(f"- Test {row['page_id']}: {row['pass_rate']:.1%}")
    lines.append("\n## Pass rate by test card\n")
    for _, row in by_card.iterrows():
        lines.append(f"- {row['test_card']}: {row['pass_rate']:.1%}")
    Path(out_md).write_text("\n".join(lines))

if __name__ == "__main__":
    summarize()
