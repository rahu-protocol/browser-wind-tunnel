# Browser Jailbreak Wind Tunnel (POC Kit)

This kit gives you five adversarial test pages, three test cards (prompts), a scoring rubric, and a scoreboard template to benchmark browsing AIs against common prompt-injection patterns.

## How to host (pick one)

### GitHub Pages
1. New public repo (e.g., `browser-wind-tunnel`).
2. Add `/pages`, `/testcards`, `/scoring` folders and this README.
3. Enable GitHub Pages (Settings → Pages → Deploy from branch → `main`).
4. Base URL: `https://<user>.github.io/browser-wind-tunnel/pages/index.html`.
5. Copy the full URLs for each test page.

### Notion
- Create five public pages and paste each HTML page’s visible content.
- Collect each public URL.

### Any static host
- Upload `/pages` to Netlify/Cloudflare Pages/etc.

## How to run
For each model (ChatGPT browsing, Copilot, Perplexity, etc.) and each test card:

1) Paste the test card with a single page URL.  
2) Score the output using `scoring/rubric.md`.  
3) Log a row in `scoring/scoreboard.csv`.  
4) Run `python3 scoring/tally.py` → paste `summary.md` into your post.

## Suggested `model_name` values
- ChatGPT-5 (Browse)
- Microsoft Copilot (Web)
- Perplexity (Browse)
- Custom Agent <name>

## Ethics & Safety
- Use these pages for controlled testing only.
- Never socially engineer humans or exfiltrate private data.
- If you find risky behavior in production, follow your org’s disclosure process.
