import httpx
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")  # optional, increases rate limit
BASE_URL = "https://api.github.com"

headers = {
    "Accept": "application/vnd.github+json",
    **({"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
}

async def get_user_profile(username: str) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/users/{username}", headers=headers)
        r.raise_for_status()
        return r.json()

async def get_user_repos(username: str) -> list:
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL}/users/{username}/repos",
            headers=headers,
            params={"sort": "updated", "per_page": 30}
        )
        r.raise_for_status()
        return r.json()

async def get_repo_languages(username: str, repo: str) -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL}/repos/{username}/{repo}/languages",
            headers=headers
        )
        r.raise_for_status()
        return r.json()

async def get_repo_commits(username: str, repo: str) -> list:
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{BASE_URL}/repos/{username}/{repo}/commits",
            headers=headers,
            params={"per_page": 5, "author": username}
        )
        r.raise_for_status()
        return r.json()