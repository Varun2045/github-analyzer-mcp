from dotenv import load_dotenv
load_dotenv()  # ← loads your .env file automatically

from mcp.server.fastmcp import FastMCP
from github_client import (
    get_user_profile,
    get_user_repos,
    get_repo_languages,
)

mcp = FastMCP("GitHub Portfolio Analyzer")


@mcp.tool()
async def analyze_github_profile(username: str) -> str:
    """
    Analyze a GitHub user's profile and return a recruiter-friendly summary.
    Includes bio, follower count, top repos, and languages used.
    """
    try:
        profile = await get_user_profile(username)
        repos = await get_user_repos(username)

        # Aggregate all languages across repos
        all_languages: dict[str, int] = {}
        top_repos = []

        for repo in repos[:10]:  # Top 10 most recently updated
            langs = await get_repo_languages(username, repo["name"])
            for lang, bytes_count in langs.items():
                all_languages[lang] = all_languages.get(lang, 0) + bytes_count

            top_repos.append({
                "name": repo["name"],
                "description": repo.get("description", "No description"),
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo.get("language", "Unknown"),
                "url": repo["html_url"],
            })

        # Sort languages by usage
        sorted_langs = sorted(
            all_languages.items(), key=lambda x: x[1], reverse=True
        )
        top_langs = [lang for lang, _ in sorted_langs[:5]]

        # Sort repos by stars
        top_repos.sort(key=lambda r: r["stars"], reverse=True)

        # Build summary
        summary = f"""
## GitHub Profile: {profile.get('name') or username}

**Handle:** @{username}
**Bio:** {profile.get('bio') or 'Not provided'}
**Location:** {profile.get('location') or 'Not specified'}
**Public Repos:** {profile.get('public_repos', 0)}
**Followers:** {profile.get('followers', 0)} | **Following:** {profile.get('following', 0)}
**Profile URL:** {profile.get('html_url')}

---

### 🛠️ Top Languages
{', '.join(top_langs) if top_langs else 'Not enough data'}

---

### ⭐ Top Repositories
"""
        for repo in top_repos[:5]:
            summary += f"""
**[{repo['name']}]({repo['url']})**
- ⭐ {repo['stars']} stars | 🍴 {repo['forks']} forks
- Language: {repo['language']}
- {repo['description']}
"""

        return summary

    except Exception as e:
        return f"Error analyzing profile: {str(e)}"


@mcp.tool()
async def compare_two_developers(username1: str, username2: str) -> str:
    """
    Compare two GitHub developers side by side.
    Great for understanding relative skill levels and focus areas.
    """
    try:
        p1, p2 = await get_user_profile(username1), await get_user_profile(username2)
        r1, r2 = await get_user_repos(username1), await get_user_repos(username2)

        def total_stars(repos):
            return sum(r["stargazers_count"] for r in repos)

        comparison = f"""
## Developer Comparison

| Metric | @{username1} | @{username2} |
|--------|------------|------------|
| Public Repos | {p1.get('public_repos', 0)} | {p2.get('public_repos', 0)} |
| Followers | {p1.get('followers', 0)} | {p2.get('followers', 0)} |
| Total Stars | {total_stars(r1)} | {total_stars(r2)} |
| Location | {p1.get('location') or 'N/A'} | {p2.get('location') or 'N/A'} |

### Top Language
- @{username1}: {r1[0].get('language') if r1 else 'N/A'}
- @{username2}: {r2[0].get('language') if r2 else 'N/A'}
"""
        return comparison

    except Exception as e:
        return f"Error comparing developers: {str(e)}"


@mcp.tool()
async def get_recruiter_summary(username: str) -> str:
    """
    Generate a polished, recruiter-ready paragraph about a developer.
    Perfect for LinkedIn recommendations or hiring assessments.
    """
    try:
        profile = await get_user_profile(username)
        repos = await get_user_repos(username)

        top_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:3]
        languages = list({r["language"] for r in repos if r.get("language")})[:5]

        summary = f"""
### 📋 Recruiter Summary for @{username}

**{profile.get('name') or username}** is a developer based in {profile.get('location') or 'an unspecified location'} 
with {profile.get('public_repos', 0)} public repositories on GitHub. 

They primarily work with: **{', '.join(languages)}**.

Their most notable projects include:
{chr(10).join(f"- **{r['name']}** ({r['stargazers_count']}⭐): {r.get('description') or 'No description'}" for r in top_repos)}

They have built a following of **{profile.get('followers', 0)} developers**, 
indicating community recognition of their work.

🔗 Full profile: {profile.get('html_url')}
"""
        return summary

    except Exception as e:
        return f"Error generating summary: {str(e)}"


if __name__ == "__main__":
    mcp.run()