# Family Tutor Telegram Bot

基于 Python Telegram Bot + DeepSeek API 的家庭辅导机器人。
适合妻子 Priska 直接在 Telegram 上使用。

## 依赖安装

```bash
pip install python-telegram-bot>=20.0 python-dotenv>=1.0.0 openai>=1.0.0
```

## 首次使用

1. 找 @BotFather (https://t.me/BotFather) 创建 bot，获取 token
2. 复制 `.env.example` 为 `.env`，填入 BOT_TOKEN 和 DEEPSEEK_API_KEY
3. 运行 `python bot.py`

## 主要功能

- 自动 AI 回复（中印尼双语，带家庭上下文）
- 快速命令：/soal（出题）、/game（游戏）、/story（故事）、/semangat（求鼓励）
