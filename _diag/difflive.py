import urllib.request, subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\difflive_out.txt'
L = ['start']
try:
    # committed index.html keywords line
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout
    L.append('COMMITTED index.html keywords:')
    L.append(g(['show', 'HEAD:index.html']).splitlines()[4] if False else '')
    for line in g(['show', 'HEAD:index.html']).splitlines():
        if 'keywords' in line.lower():
            L.append(line[:400])
    # live
    req = urllib.request.Request('https://toolstack.dpdns.org/', headers={'User-Agent':'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')
    L.append('LIVE keywords line:')
    for line in html.splitlines():
        if 'keywords' in line.lower():
            L.append(line[:400])
    # also check the age-calc live vs committed
    L.append('--- age-calc ---')
    req2 = urllib.request.Request('https://toolstack.dpdns.org/tools/age-calc/', headers={'User-Agent':'Mozilla/5.0'})
    html2 = urllib.request.urlopen(req2, timeout=30).read().decode('utf-8','ignore')
    for line in html2.splitlines():
        if 'keywords' in line.lower() or 'og:site_name' in line.lower():
            L.append(line[:400])
    L.append('COMMITTED age-calc keywords:')
    for line in g(['show', 'HEAD:tools/age-calc/index.html']).splitlines():
        if 'keywords' in line.lower() or 'og:site_name' in line.lower():
            L.append(line[:400])
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT,'w').write('\n'.join(L))
print('WROTE', len(L))