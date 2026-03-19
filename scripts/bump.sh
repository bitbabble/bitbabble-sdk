#!/usr/bin/env bash
# Bump versions in both JavaScript and Python packages.
# Usage: ./scripts/bump.sh [patch|minor|major]  (default: patch)

set -e
PART=${1:-patch}

cd "$(dirname "$0")/../packages/javascript"
NEW_VERSION=$(npm version "$PART" --no-git-tag-version | sed 's/^v//')
cd ../..

# Update Python package to match
if [[ "$OSTYPE" == "darwin"* ]]; then
  sed -i '' "s/^version = \".*\"/version = \"$NEW_VERSION\"/" packages/python/pyproject.toml
else
  sed -i "s/^version = \".*\"/version = \"$NEW_VERSION\"/" packages/python/pyproject.toml
fi

echo "Bumped to $NEW_VERSION"
