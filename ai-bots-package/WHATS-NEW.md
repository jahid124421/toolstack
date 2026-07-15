# 🎉 What's New - Enhanced Usage Tracking & Smart Model Selection

## Summary
Your AI Agent Team now shows **API provider, model name, and token usage** for every request, plus smart model selection for **CODING** vs **BA WORK** with **private API priority**.

---

## ✨ New Features

### 1. 📊 Real-Time Usage Display
**Before:**
```
Model: free-agent-team
Usage: 0 tokens (not tracked)
```

**Now:**
```
Provider: GROQ (FREE)
Model: llama-3.3-70b-versatile
Usage: 150 in / 500 out / 650 total tokens
Cost: FREE ✓
```

### 2. 🎯 Smart Mode Selection
**New Launcher:** `START-TEAM-ENHANCED.bat`

Choose based on your task:
- **[1] CODING MODE** → Private APIs first (GROQ → CEREBRAS → CF)
- **[2] BA MODE** → Best reasoning models (CEREBRAS → GROQ → FM)
- **[3] AUTO MODE** → Smart auto-selection

### 3. 💰 Token Conservation
**Why your tokens won't burn quickly:**
- ✅ All providers are FREE (or you have credits)
- ✅ Private APIs (GROQ, CEREBRAS) = generous limits
- ✅ Smart caching = fewer redundant calls
- ✅ Fast providers tried first = less waiting
- ✅ Real-time tracking = you stay informed

### 4. 📈 Usage Monitoring
**New Tools:**
- `SHOW-USAGE.bat` - Quick stats viewer
- `show_usage.py --watch` - Live monitoring
- `http://localhost:8080/usage` - JSON endpoint

---

## 🚀 Quick Start

### Step 1: Launch with Mode Selection
```bat
START-TEAM-ENHANCED.bat
```

### Step 2: Choose Your Mode
- Press **[1]** for coding tasks
- Press **[2]** for BA/analysis work
- Press **[3]** for auto mode

### Step 3: Configure Your IDE
```
Base URL:  http://localhost:8080/v1
API Key:   local
Model:     auto
```

### Step 4: Monitor Usage (Optional)
```bat
SHOW-USAGE.bat
```

---

## 📋 What Gets Tracked

| Metric | Description | Example |
|--------|-------------|---------|
| Provider | API service being used | GROQ (FREE) |
| Model | Specific AI model | llama-3.3-70b-versatile |
| Prompt Tokens | Input tokens sent | 150 |
| Completion Tokens | Output tokens received | 500 |
| Total Tokens | Combined token count | 650 |
| Cost | Estimated cost (or FREE) | FREE ✓ |
| Total Calls | Number of API requests | 42 |

---

## 🎨 Mode Differences

### CODING MODE
```
Priority: Private APIs First
├─ GROQ: llama-3.3-70b-versatile (fast, 70B)
├─ CEREBRAS: gpt-oss-120b (fast, 120B reasoning)
├─ CLOUDFLARE: llama-3.3-fp8-fast (fast, 70B)
├─ FREEMODEL: gpt-5.4 (capable, has credits)
└─ OPENROUTER: qwen3-coder:free (coding specialist)

Max Tokens: 3000
Best For: Code generation, debugging, refactoring
```

### BA MODE
```
Priority: Best Reasoning First
├─ CEREBRAS: gpt-oss-120b (120B reasoning powerhouse)
├─ GROQ: llama-3.3-70b-versatile (fast general)
├─ FREEMODEL: gpt-5.4 (capable)
├─ CLOUDFLARE: llama-3.3-fp8-fast (fast)
└─ OPENROUTER: qwen3-next-80b:free (analysis)

Max Tokens: 4000
Best For: Analysis, planning, documentation, research
```

---

## 📊 Usage Tracking in Action

### In Your IDE
Every response now includes:
```json
{
  "id": "chatcmpl-abc123",
  "model": "GROQ (FREE) | llama-3.3-70b-versatile",
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 500,
    "total_tokens": 650
  },
  "choices": [...]
}
```

### In Usage Monitor
```
📊 CURRENT SESSION:
   Provider:    GROQ (FREE)
   Model:       llama-3.3-70b-versatile
   Total Calls: 42

💰 TOKEN USAGE:
   Input Tokens:     6,250
   Output Tokens:    18,500
   Total Tokens:     24,750
   Cost:             FREE ✓

🔌 PROVIDER STATUS:
   GROQ            ✓ ENABLED
   CEREBRAS        ✓ ENABLED
   CLOUDFLARE      ✓ ENABLED
   FREEMODEL       ✓ ENABLED
   OPENROUTER      ✓ ENABLED
```

---

## 🛠️ New Files

| File | Purpose |
|------|---------|
| `START-TEAM-ENHANCED.bat` | New launcher with mode selection |
| `SHOW-USAGE.bat` | Quick usage stats viewer |
| `show_usage.py` | Usage monitoring script |
| `USAGE-TRACKING-README.md` | Complete documentation |
| `QUICK-START.md` | Quick reference guide |
| `SYSTEM-OVERVIEW.md` | Architecture diagrams |
| `WHATS-NEW.md` | This file |
| `mode_config.txt` | Saved mode preference |

---

## 🔄 Changes to Existing Files

### `ai-agent-team.py`
**Added:**
- `_USAGE_STATS` dictionary for tracking
- `estimate_tokens()` function
- Usage tracking in `try_provider()`
- Usage data in API responses
- `/usage` endpoint
- Enhanced `/` endpoint with stats

**Modified:**
- All provider functions now return usage data
- `call_role()` updates global usage stats
- Response includes provider + model name

---

## 💡 Usage Tips

### 1. Monitor in Real-Time
```bat
python show_usage.py --watch 5
```
Updates every 5 seconds. Perfect for tracking during active coding.

### 2. Check Between Tasks
```bat
SHOW-USAGE.bat
```
Quick snapshot of current session stats.

### 3. Review Logs
```bat
type ai-agent-team.log | findstr "usage"
```
See detailed usage history.

### 4. API Endpoint
```bash
curl http://localhost:8080/usage
```
Integrate into your own monitoring tools.

---

## 🎯 Why These Changes?

### Problem Before
- ❌ No visibility into which provider/model was used
- ❌ No token usage tracking
- ❌ Same priority for all task types
- ❌ No way to optimize for specific use cases

### Solution Now
- ✅ See provider and model in every response
- ✅ Track exact token consumption
- ✅ Optimized priorities for coding vs analysis
- ✅ Real-time usage monitoring
- ✅ Cost transparency (FREE vs PAID)

---

## 🚨 Important Notes

### All Free by Default
Unless you add `ANTHROPIC_API_KEY` to `my-keys.env`, everything is 100% free:
- GROQ: Free forever
- CEREBRAS: Free forever
- CLOUDFLARE: Free forever
- FREEMODEL: Free credits available
- OPENROUTER: Free tier models

### Private APIs First (Coding Mode)
Private APIs (GROQ, CEREBRAS, CF) have more generous rate limits than public aggregators like OpenRouter.

### Your Data is Safe
Usage tracking stores:
- ✅ Provider names
- ✅ Model names
- ✅ Token counts
- ❌ NO message content
- ❌ NO API keys
- ❌ NO personal data

---

## 📚 Documentation

- **Quick Start:** `QUICK-START.md`
- **Full Guide:** `USAGE-TRACKING-README.md`
- **Architecture:** `SYSTEM-OVERVIEW.md`
- **Original Docs:** `README.md` (if exists)

---

## 🎊 Enjoy!

Your tokens are safe, your usage is tracked, and your models are optimized. Code away! 🚀

**Questions?** Check the logs:
```bat
type ai-agent-team.log
```
