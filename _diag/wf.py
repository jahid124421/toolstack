import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\wf_out.txt'

L = ['start']
try:
    wfdir = os.path.join(R, '.github', 'workflows')
    files = os.listdir(wfdir) if os.path.isdir(wfdir) else []
    L.append('workflow files: ' + repr(files))
    for f in files:
        p = os.path.join(wfdir, f)
        L.append('===== ' + f + ' =====')
        L.append(open(p, 'r', encoding='utf-8').read()[:2000])
        L.append('')
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))