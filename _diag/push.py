import subprocess, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\push_out.txt'

L = ['start']
try:
    def run(args):
        r = subprocess.run(['git', '-C', R] + args, capture_output=True, text=True)
        return f'rc={r.returncode}\n{r.stdout.strip()}\n{r.stderr.strip()}'

    L.append('ADD: ' + run(['add', '-A']))
    L.append('COMMIT: ' + run(['commit', '-m', 'Complete ToolStack rebrand: remove all remaining Somar branding across 213 files (HTML, JS, build script, docs)']))
    L.append('PUSH: ' + run(['push', 'origin', 'main']))
    L.append('LOG: ' + subprocess.run(['git', '-C', R, 'log', '--oneline', '-3'], capture_output=True, text=True).stdout.strip())
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))