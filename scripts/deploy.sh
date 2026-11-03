#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="$1"; TAG="$2"; PORT="$3"
PROJECT="rks506-${ENV_NAME}"
STATE_DIR="${HOME}/.rks506"
STATE_FILE="${STATE_DIR}/${ENV_NAME}.current"
mkdir -p "$STATE_DIR"
PREV="$(cat "$STATE_FILE" 2>/dev/null || true)"

export APP_ENV="$ENV_NAME" PORT

# Fail early if this image was never built (e.g. tagging something that skipped staging)
docker image inspect "rks506-app:${TAG}" >/dev/null

TAG="$TAG" docker compose -p "$PROJECT" up -d --remove-orphans

for _ in $(seq 1 15); do
  if curl -fs "http://127.0.0.1:${PORT}/health" | grep -q '"ok"'; then
    echo "$TAG" > "$STATE_FILE"
    echo "Deployed ${TAG} to ${ENV_NAME}"
    exit 0
  fi
  sleep 2
done

echo "Deploy failed for ${ENV_NAME}"
TAG="$TAG" docker compose -p "$PROJECT" logs --tail 50 app || true
if [ -n "$PREV" ]; then
  echo "Rolling back to ${PREV}"
  TAG="$PREV" docker compose -p "$PROJECT" up -d
fi
exit 1

