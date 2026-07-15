import urllib.request, re, traceback

OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\findsomar_out.txt'
L = ['start']
try:
    u = 'https://toolstack.dpdns.org/'
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')
    for m in re.finditer(r'somar', html, re.IGNORECASE):
        s = max(0, m.start()-80)
        e = min(len(html), m.end()+80)
        L.append('...' + html[s:e] + '...')
        L.append('---')
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))