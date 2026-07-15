import subprocess, os, traceback
from collections import Counter

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\out3.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    res = g(['grep', '-i', '-l', 'somar', 'HEAD', '--'])
    files = [x for x in res.splitlines() if x.strip()]
    L.append('HEAD files containing somar (any case): ' + str(len(files)))
    ext = Counter(os.path.splitext(f)[1] or 'NONE' for f in files)
    L.append('by ext: ' + repr(dict(ext)))

    pat = r"somar[a-z's]*"
    alltext = g(['grep', '-i', '-o', pat, 'HEAD', '--'])
    pc = Counter(x.strip().lower() for x in alltext.splitlines() if x.strip())
    L.append('distinct somar patterns (HEAD): ' + repr(pc.most_common(25)))

    wt = g(['grep', '-i', '-o', pat, '--'])
    pcw = Counter(x.strip().lower() for x in wt.splitlines() if x.strip())
    L.append('distinct somar patterns (WORKING): ' + repr(pcw.most_common(25)))

    names = g(['diff', '--name-only']).splitlines()
    L.append('unstaged names count=' + str(len(names)))

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))