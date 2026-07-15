"""
show_usage.py - Display real-time usage statistics from AI Agent Team
"""

import requests
import json
import sys
import time
from datetime import datetime

SERVER_URL = "http://localhost:8080"

def format_number(num):
    """Format large numbers with commas"""
    return f"{num:,}"

def display_usage():
    """Fetch and display usage statistics"""
    try:
        # Get usage stats
        response = requests.get(f"{SERVER_URL}/usage", timeout=5)
        if response.status_code != 200:
            print(f"Error: Server returned status {response.status_code}")
            return False
        
        stats = response.json()
        
        # Get server info
        info_response = requests.get(f"{SERVER_URL}/", timeout=5)
        info = info_response.json() if info_response.status_code == 200 else {}
        
        # Clear screen (Windows)
        print("\033[2J\033[H", end="")
        
        # Display header
        print("=" * 70)
        print(" " * 15 + "AI AGENT TEAM - USAGE STATISTICS")
        print("=" * 70)
        print(f"\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 70)
        
        # Display current session info
        print("\n📊 CURRENT SESSION:")
        print(f"   Provider:    {stats.get('current_provider', 'N/A')}")
        print(f"   Model:       {stats.get('current_model', 'N/A')}")
        print(f"   Total Calls: {format_number(stats.get('total_requests', 0))}")
        
        # Display token usage
        print("\n💰 TOKEN USAGE:")
        prompt_tokens = stats.get('prompt_tokens', 0)
        completion_tokens = stats.get('completion_tokens', 0)
        total_tokens = stats.get('total_tokens', 0)
        
        print(f"   Input Tokens:     {format_number(prompt_tokens)}")
        print(f"   Output Tokens:    {format_number(completion_tokens)}")
        print(f"   Total Tokens:     {format_number(total_tokens)}")
        
        # Calculate estimated costs (if using paid APIs)
        if stats.get('current_provider') == 'ANTHROPIC (PAID)':
            # Rough estimate: $3 per 1M input tokens, $15 per 1M output tokens for Claude Sonnet
            cost_estimate = (prompt_tokens * 3 / 1_000_000) + (completion_tokens * 15 / 1_000_000)
            print(f"   Est. Cost:        ${cost_estimate:.4f} USD")
        else:
            print(f"   Cost:             FREE ✓")
        
        # Display provider status
        print("\n🔌 PROVIDER STATUS:")
        providers = info.get('providers', {})
        for provider, enabled in providers.items():
            status = "✓ ENABLED" if enabled else "✗ DISABLED"
            print(f"   {provider.upper():15} {status}")
        
        # Display cached models per role
        print("\n🤖 CACHED MODELS BY ROLE:")
        roles = info.get('roles', {})
        for role, role_info in roles.items():
            cached = role_info.get('cached', 'none')
            print(f"   {role:12} → {cached}")
        
        print("\n" + "=" * 70)
        print(f"Server: {SERVER_URL}")
        print("Press Ctrl+C to exit")
        print("=" * 70)
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to AI Agent Team server.")
        print(f"Make sure the server is running at {SERVER_URL}")
        return False
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

def continuous_monitor(interval=5):
    """Monitor usage continuously"""
    print("Starting continuous monitoring...")
    print(f"Refresh interval: {interval} seconds\n")
    
    try:
        while True:
            if not display_usage():
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        # Continuous monitoring mode
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        continuous_monitor(interval)
    else:
        # One-time display
        display_usage()
