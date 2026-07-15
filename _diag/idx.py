import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\idx_out.txt'
L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    L.append('=== working index.html keywords/title lines ===')
    p = os.path.join(R, 'index.html')
    txt = open(p, 'r', encoding='utf-8').read()
    for line in txt.splitlines():
        if 'keyword' in line.lower() or 'somar' in line.lower() or 'toolstack' in line.lower():
            L.append(line[:300])
    L.append('=== git grep somar in index.html (HEAD) ===')
    L.append(g(['grep', '-i', 'somar', 'HEAD', '--', 'index.html']).strip() or 'NONE')
    L.append('=== git grep somar in index.html (working) ===')
    L.append(g(['grep', '-i', 'somar', '--', 'index.html']).strip() or 'NONE')
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))