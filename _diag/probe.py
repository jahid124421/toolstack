import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\out.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    L.append('HEAD=' + g(['rev-parse', '--short', 'HEAD']).strip())
    L.append('BRANCH=' + g(['rev-parse', '--abbrev-ref', 'HEAD']).strip())
    L.append('LOG3=' + g(['log', '--oneline', '-3']).strip())

    names = g(['diff', '--name-only']).splitlines()
    L.append('UNSTAGED_names=' + str(len(names)))
    L.append('first5=' + repr(names[:5]))

    p = os.path.join(R, 'index.html')
    raw = open(p, 'rb').read(400)
    L.append('work_crlf=' + str(raw[:2] == b'\r\n'))
    cb = subprocess.run(['git', '-C', R, 'show', 'HEAD:index.html'], capture_output=True).stdout[:400]
    L.append('commit_crlf=' + str(cb[:2] == b'\r\n'))
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L), 'lines')