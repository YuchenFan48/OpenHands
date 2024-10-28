#!/bin/bash

# 将所有参数组合为一个字符串
PROMPT="$*"

if [ -z "$PROMPT" ]; then
    echo "Usage: $0 \"your prompt text\""
    exit 1
fi

# 执行 OpenHands 命令
python -m openhands.core.main -t "$PROMPT"
