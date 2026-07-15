import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\gitinfo_out.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    L.append('REMOTE:')
    L.append(g(['remote', '-v']).strip())
    L.append('BRANCH:')
    L.append(g(['branch', '-vv']).strip())
    L.append('STATUS:')
    L.append(g(['status', '-s']).strip()[:500])
    # deploy files present?
    for f in ['.github/workflows', 'wrangler.toml', 'vercel.json', 'netlify.toml', 'deploy']:
        p = os.path.join(R, f)
        L.append(f + ' exists=' + str(os.path.exists(p)))

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))