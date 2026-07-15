import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\last_out.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    rem = [x for x in g(['grep', '-i', '-n', 'somar', '--']).splitlines() if x.strip()]
    L.append('ALL remaining somar lines:')
    L.append('\n'.join(rem))

    # confirm rename_website.py is the only file
    files = set(x.split(':')[0] for x in rem)
    L.append('files with somar: ' + repr(files))

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))