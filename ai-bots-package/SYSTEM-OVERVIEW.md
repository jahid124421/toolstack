# 🏗️ System Architecture Overview

## Request Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         YOUR IDE                                │
│                  (Cline/Continue/Cursor)                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │ HTTP Request
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              AI AGENT TEAM SERVER (Port 8080)                   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  1. Request Router                                       │  │
│  │     • Parse request                                      │  │
│  │     • Identify mode (CODING/BA/AUTO)                     │  │
│  │     • Select role (think/code/multitask/fetch/automate) │  │
│  └─────────────────┬───────────────────────────────────────┘  │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  2. Provider Selector                                    │  │
│  │     • Check cached working model for role                │  │
│  │     • Try providers in priority order:                   │  │
│  │       CODING:  GROQ → CEREBRAS → CF → FM → OR          │  │
│  │       BA:      CEREBRAS → GROQ → FM → CF → OR          │  │
│  │       AUTO:    Best available                            │  │
│  └─────────────────┬───────────────────────────────────────┘  │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  3. API Call Handler                                     │  │
│  │     • Send request to selected provider                  │  │
│  │     • Track usage (provider, model, tokens)              │  │
│  │     • Cache successful model for next time               │  │
│  │     • Fallback to next provider if failed                │  │
│  └─────────────────┬───────────────────────────────────────┘  │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  4. Usage Tracker                                        │  │
│  │     _USAGE_STATS = {                                     │  │
│  │       "total_requests": 42,                              │  │
│  │       "current_provider": "GROQ (FREE)",                 │  │
│  │       "current_model": "llama-3.3-70b-versatile",        │  │
│  │       "prompt_tokens": 6250,                             │  │
│  │       "completion_tokens": 18500,                        │  │
│  │       "total_tokens": 24750                              │  │
│  │     }                                                     │  │
│  └─────────────────┬───────────────────────────────────────┘  │
│                    │                                            │
│                    ▼                                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  5. Response Builder                                     │  │
│  │     • Format response with usage data                    │  │
│  │     • Include provider & model in response               │  │
│  │     • Return to IDE                                      │  │
│  └─────────────────┬───────────────────────────────────────┘  │
└────────────────────┼────────────────────────────────────────────┘
                     │
                     │ HTTP Response with Usage Data
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                   IDE DISPLAYS RESULT                           │
│                                                                 │
│  Model: GROQ (FREE) | llama-3.3-70b-versatile                  │
│  Usage: 150 in / 500 out / 650 total                           │
│  Cost:  FREE ✓                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Provider Priority by Mode

### CODING MODE
```
PRIVATE APIs FIRST (Fast, Generous Limits)
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   GROQ       │ ──> │  CEREBRAS    │ ──> │ CLOUDFLARE   │
│ llama-3.3-70b│     │ gpt-oss-120b │     │ llama-3.3-fp8│
│   (FREE)     │     │   (FREE)     │     │   (FREE)     │
└──────────────┘     └──────────────┘     └──────────────┘
        │                                         │
        └─────────────┬───────────────────────────┘
                      ▼
            ┌──────────────┐     ┌──────────────┐
            │  FREEMODEL   │ ──> │ OPENROUTER   │
            │  gpt-5.4     │     │ qwen3-coder  │
            │  (CREDITS)   │     │   (FREE)     │
            └──────────────┘     └──────────────┘
```

### BA MODE
```
REASONING FIRST (Best for Analysis)
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  CEREBRAS    │ ──> │    GROQ      │ ──> │  FREEMODEL   │
│ gpt-oss-120b │     │ llama-3.3-70b│     │   gpt-5.4    │
│   (FREE)     │     │   (FREE)     │     │  (CREDITS)   │
└──────────────┘     └──────────────┘     └──────────────┘
        │                                         │
        └─────────────┬───────────────────────────┘
                      ▼
            ┌──────────────┐     ┌──────────────┐
            │ CLOUDFLARE   │ ──> │ OPENROUTER   │
            │ llama-3.3-fp8│     │   qwen3-next │
            │   (FREE)     │     │   (FREE)     │
            └──────────────┘     └──────────────┘
```

## Usage Tracking Flow

```
┌─────────────────────────────────────────────────────────────┐
│  API Call Made                                              │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Provider Returns Response + Usage Data                     │
│  {                                                           │
│    "model": "llama-3.3-70b-versatile",                      │
│    "usage": {                                               │
│      "prompt_tokens": 150,                                  │
│      "completion_tokens": 500,                              │
│      "total_tokens": 650                                    │
│    }                                                         │
│  }                                                           │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Update Global _USAGE_STATS                                 │
│    total_requests += 1                                      │
│    current_provider = "GROQ (FREE)"                         │
│    current_model = "llama-3.3-70b-versatile"                │
│    prompt_tokens += 150                                     │
│    completion_tokens += 500                                 │
│    total_tokens += 650                                      │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Log to File                                                │
│  [2026-07-14 10:30:45] [usage] GROQ (FREE) |               │
│  llama-3.3-70b-versatile | in:150 out:500 total:650        │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ├──────────────────┬─────────────────────┐
                    ▼                  ▼                     ▼
          ┌─────────────────┐  ┌─────────────┐  ┌──────────────┐
          │ Return to IDE   │  │ /usage      │  │ show_usage.py│
          │ with usage data │  │ endpoint    │  │ displays it  │
          └─────────────────┘  └─────────────┘  └──────────────┘
```

## File Structure

```
ai-bots-package/
├── ai-agent-team.py           ← Main server with usage tracking
├── START-TEAM-ENHANCED.bat    ← New launcher with mode selection
├── SHOW-USAGE.bat             ← Quick usage stats viewer
├── show_usage.py              ← Usage monitoring script
├── mode_config.txt            ← Saved mode preference
├── current_model.txt          ← Current model selection
├── my-keys.env                ← API keys (keep private!)
├── available_models.json      ← List of available models
├── ai-agent-team.log          ← Server logs with usage
│
├── USAGE-TRACKING-README.md   ← Full documentation
├── QUICK-START.md             ← Quick reference
└── SYSTEM-OVERVIEW.md         ← This file
```

## Key Components

### 1. Usage Stats Dictionary
```python
_USAGE_STATS = {
    "total_requests": 0,        # Total API calls made
    "current_provider": None,   # Last provider used
    "current_model": None,      # Last model used
    "prompt_tokens": 0,         # Total input tokens
    "completion_tokens": 0,     # Total output tokens
    "total_tokens": 0,          # Total tokens
}
```

### 2. Provider Try Function
```python
def try_provider(model_name, provider_type, messages, max_tokens):
    # ... make API call ...
    if success:
        usage_dict = {
            "provider": "GROQ (FREE)",
            "model": model_name,
            "prompt_tokens": 150,
            "completion_tokens": 500,
            "total_tokens": 650,
        }
        return content, None, usage_dict
```

### 3. Usage Endpoints
```python
@app.route("/usage")  # GET /usage
def usage():
    return jsonify(_USAGE_STATS)

@app.route("/")       # GET /
def home():
    return jsonify({
        "usage": _USAGE_STATS,
        # ... other info ...
    })
```

## Benefits

✅ **Token Efficiency**
- Smart caching reduces redundant calls
- Fast providers tried first (less waiting time)
- Private APIs have generous free limits

✅ **Transparency**
- See exactly which provider and model is being used
- Track token consumption in real-time
- Know if you're using free or paid APIs

✅ **Flexibility**
- Choose mode based on task type
- Switch modes without restarting
- Auto-fallback if provider fails

✅ **Cost Control**
- All free by default
- Clear indication when using paid APIs
- Accurate cost estimation for paid providers
