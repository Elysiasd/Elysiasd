#!/usr/bin/env bash
# 拉取两个账号的贡献日历到 data/，供 gen_contrib.py 合并。
# 需要环境变量 GH_TOKEN（Actions 里用内置 GITHUB_TOKEN）。
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p data

ACCOUNTS=("${GH_ACCOUNT:-Elysiasd}" "yujiezhang-ops")

for i in "${!ACCOUNTS[@]}"; do
  login="${ACCOUNTS[$i]}"
  out="data/$([ "$i" -eq 0 ] && echo ely || echo ops).json"
  gh api graphql -f query="
    query {
      user(login: \"$login\") {
        contributionsCollection {
          contributionCalendar {
            weeks { contributionDays { date contributionCount } }
          }
        }
      }
    }" --jq '[.data.user.contributionsCollection.contributionCalendar.weeks[].contributionDays[]]' > "$out"
  echo "$login -> $out ($(python3 -c "import json,sys;print(len(json.load(open('$out'))))") days)"
done
