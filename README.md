<h3 align="center">🔍 GitHub Portfolio Analyzer — MCP Server</h3>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<div align="center">

**An MCP (Model Context Protocol) server that lets Claude AI analyze GitHub profiles and generate recruiter-ready developer summaries.**

</div>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<h3 align="center">🚀 What It Does</h3>

<div align="center">

*"Analyze the GitHub profile of torvalds"*

*"Compare developers gvanrossum and dhh"*

*"Give me a recruiter summary for sindresorhus"*

</div>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<h3 align="center">🛠️ Tech Stack</h3>

<div align="center">

Python 3.10+

[MCP SDK](https://github.com/anthropics/mcp) by Anthropic

GitHub REST API v3

httpx (async HTTP)

Claude Desktop (host)

</div>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<h3 align="center">⚙️ Setup</h3>

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/github-analyzer-mcp
cd github-analyzer-mcp
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your GitHub token**
```bash
cp .env.example .env
# Edit .env and add your GITHUB_TOKEN
```

**4. Add to Claude Desktop config**
```json
{
  "mcpServers": {
    "github-analyzer": {
      "command": "python",
      "args": ["C:\\path\\to\\server.py"]
    }
  }
}
```

**5.** Restart Claude Desktop and start analyzing!

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<h3 align="center">🔧 Available Tools</h3>

<div align="center">

| Tool | Description |
|------|-------------|
| `analyze_github_profile` | Full profile breakdown with top repos & languages |
| `compare_two_developers` | Side-by-side comparison table |
| `get_recruiter_summary` | Polished paragraph for hiring decisions |

</div>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<h3 align="center">📸 Demo</h3>

<div align="center">

<h4>✅ MCP Server Connected & Running</h4>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<br>

<img src="screenshots/server-running.png" alt="Server Running" width="700"/>

<h4>🔍 Analyzing Linus Torvalds' Profile</h4>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<br>

<img src="screenshots/torvalds-analysis.png" alt="Torvalds Analysis" width="700"/>
<img src="screenshots/torvalds-analysis-2.png" alt="Torvalds Analysis 2" width="700"/>

<h4>⚖️ Comparing Two Developers</h4>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<br>

<img src="screenshots/compare-developers.png" alt="Compare Developers" width="700"/>

<h4>📋 Recruiter Summary Output</h4>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<br>

<img src="screenshots/recruiter-summary.png" alt="Recruiter Summary" width="700"/>

<h4>👤 Analyzing My Own Profile</h4>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>

<br>

<img src="screenshots/varun-analysis.png" alt="Varun Analysis" width="700"/>
<img src="screenshots/varun-analysis-2.png" alt="Varun Analysis 2" width="700"/>

</div>

<div align="center"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></div>
