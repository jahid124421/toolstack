# 🚀 QUICK START GUIDE

## For Coding Tasks
```bat
START-TEAM-ENHANCED.bat
→ Press [1] for CODING MODE
→ Uses: GROQ → CEREBRAS → CLOUDFLARE (Private APIs First)
```

## For Business Analyst Work
```bat
START-TEAM-ENHANCED.bat
→ Press [2] for BA MODE
→ Uses: CEREBRAS → GROQ → FREEMODEL (Best for Analysis)
```

## Check Usage Stats
```bat
SHOW-USAGE.bat
```

Or visit: `http://localhost:8080/usage`

## What You'll See

### In IDE (Cline/Continue/Cursor):
```
Provider: GROQ (FREE)
Model: llama-3.3-70b-versatile
Tokens: 150 in / 500 out / 650 total
```

### In Usage Monitor:
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
```

## IDE Settings
```
Base URL:  http://localhost:8080/v1
API Key:   local  
Model:     auto
```

## Priority Orders

### CODING MODE
1. GROQ (fast, free, 70B)
2. CEREBRAS (fast, free, 120B)
3. CLOUDFLARE (fast, free, 70B)
4. FREEMODEL (fast, has credits)
5. OpenRouter (slow, free)

### BA MODE
1. CEREBRAS (best reasoning, 120B)
2. GROQ (fast general purpose, 70B)
3. FREEMODEL (capable, has credits)
4. CLOUDFLARE (fast, 70B)
5. OpenRouter (diverse models, free)

## Done! 🎉

Your tokens won't burn quickly because:
- ✅ All providers are FREE (or you have credits)
- ✅ Smart caching reduces redundant calls
- ✅ Fast providers tried first (less waiting)
- ✅ Usage tracking helps you monitor consumption
- ✅ Private APIs (GROQ, CEREBRAS) have generous limits
