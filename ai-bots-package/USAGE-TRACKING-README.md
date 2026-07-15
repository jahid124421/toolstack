# AI Agent Team - Enhanced Usage Tracking & Model Selection

## 🎯 New Features

### 1. Real-Time Usage Tracking
The system now tracks and displays:
- **API Provider Name** (GROQ, CEREBRAS, CLOUDFLARE, FREEMODEL, OPENROUTER, ANTHROPIC)
- **Model Name** (e.g., llama-3.3-70b-versatile, gpt-oss-120b)
- **Token Usage**:
  - Input/Prompt tokens
  - Output/Completion tokens
  - Total tokens
- **Cost Tracking** (for paid APIs like Anthropic Claude)
- **Total API Calls** made in session

### 2. Categorized Model Selection
Choose the best models for your specific task:

#### **CODING MODE** (Private APIs First)
Best for: Code generation, debugging, refactoring, technical implementation
- Priority: GROQ → CEREBRAS → CLOUDFLARE → FREEMODEL → OpenRouter
- Optimized for fast, accurate code completion
- Max tokens: 3000 per call

#### **BUSINESS ANALYST MODE**
Best for: Analysis, planning, documentation, requirements gathering, research
- Priority: CEREBRAS → GROQ → FREEMODEL → CLOUDFLARE → OpenRouter
- Optimized for reasoning and comprehensive analysis
- Max tokens: 4000 per call

#### **AUTO MODE**
Let the system intelligently choose based on availability and response time
- Max tokens: 2000 per call

## 📊 How to View Usage Stats

### Option 1: Check in IDE Response
Usage info is now included in every API response:
```json
{
  "model": "GROQ (FREE) | llama-3.3-70b-versatile",
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 500,
    "total_tokens": 650
  }
}
```

### Option 2: Usage Endpoint
Visit in browser or use curl:
```
http://localhost:8080/usage
```

### Option 3: Usage Monitor Script
Run the usage monitor BAT file:
```
SHOW-USAGE.bat
```

Or run continuously (updates every 5 seconds):
```
python show_usage.py --watch 5
```

### Option 4: Server Home Page
Visit the server status page:
```
http://localhost:8080/
```

## 🚀 Quick Start

### Using the Enhanced Launcher
1. Run `START-TEAM-ENHANCED.bat`
2. Choose your mode:
   - **[1]** For coding tasks
   - **[2]** For business analyst work
   - **[3]** For auto mode
3. The server starts with optimized settings

### IDE Configuration
```
Base URL:  http://localhost:8080/v1
API Key:   local
Model:     auto (or specific model from menu)
```

## 📈 Usage Tracking Details

### What Gets Tracked
- ✅ Provider name (GROQ, CEREBRAS, etc.)
- ✅ Model name (llama-3.3-70b-versatile, etc.)
- ✅ Input tokens (prompt)
- ✅ Output tokens (completion)
- ✅ Total tokens
- ✅ Total API calls
- ✅ Cached models per role

### What Doesn't Get Tracked
- ❌ Personal/private data
- ❌ API keys
- ❌ Message content
- ❌ User information

### Where Data is Stored
- In-memory only (resets when server restarts)
- Log file: `ai-agent-team.log` (text only, no sensitive data)

## 💡 Pro Tips

### 1. Monitor Token Usage
Keep `show_usage.py --watch 5` running in a separate window to monitor usage in real-time

### 2. Choose the Right Mode
- **Coding Mode**: Use when you need precise, executable code
- **BA Mode**: Use for analysis, documentation, planning
- **Auto Mode**: Use for general mixed tasks

### 3. Check Provider Status
If a provider seems slow, check `http://localhost:8080/` to see which providers are enabled

### 4. Log Analysis
Review `ai-agent-team.log` to see:
- Which models are being cached
- Response times
- Any errors or rate limits

## 🔧 Advanced Configuration

### Environment Variables
You can override settings:
```
set TEAM_MAX_TOKENS=5000
set PRIMARY_PROVIDER=CEREBRAS
```

### Custom Model Priority
Edit `ai-agent-team.py` to reorder `ALL_MODELS` list

### Mode Persistence
Your last mode choice is saved in `mode_config.txt`

## 🐛 Troubleshooting

### Usage shows zeros
- Make sure you've made at least one API call
- Check if server is running: `http://localhost:8080/`

### Provider shows "unknown"
- First API call hasn't completed yet
- Check logs: `ai-agent-team.log`

### Cost shows for free APIs
- Should always show "FREE ✓" for GROQ, CEREBRAS, CLOUDFLARE, FREEMODEL, OPENROUTER
- Only shows cost for ANTHROPIC (PAID) when using Claude with API key

## 📝 Changelog

### v2.0 - Enhanced Tracking & Selection
- ✅ Added real-time usage tracking
- ✅ Added provider and model name display
- ✅ Added categorized model selection (Coding vs BA)
- ✅ Added usage monitoring script
- ✅ Added cost tracking for paid APIs
- ✅ Enhanced BAT launcher with mode selection
- ✅ Added usage endpoint `/usage`

---

## 🤝 Support

Check logs if issues occur:
```
type ai-agent-team.log
```

For model issues, verify providers:
```
python fetch_models.py
```
