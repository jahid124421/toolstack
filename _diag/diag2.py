import urllib.request, subprocess, json, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\diag2_out.txt'
L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout

    L.append('=== git log (recent) ===')
    L.append(g(['log', '--oneline', '-8']).strip())

    # committed index.html length + keywords
    idx = g(['show', 'HEAD:index.html'])
    L.append('HEAD index.html len=' + str(len(idx)))
    for line in idx.splitlines():
        if 'keywords' in line.lower():
            L.append('HEAD keywords: ' + line[:200])

    # live with cache-bust
    for q in ['?cb=1', '?cb=2']:
        try:
            req = urllib.request.Request('https://toolstack.dpdns.org/'+q, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
            h = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')
            L.append('LIVE'+q+' len='+str(len(h))+' somar='+str(h.lower().count('somar')))
            for line in h.splitlines():
                if 'keywords' in line.lower():
                    L.append('LIVE'+q+' keywords: '+line[:200])
        except Exception as e:
            L.append('LIVE'+q+' ERR='+repr(e))

    # DNS
    L.append('=== DNS toolstack.dpdns.org ===')
    import socket
    try:
        L.append('A/AAAA: ' + str(socket.getaddrinfo('toolstack.dpdns.org', None)))
    except Exception as e:
        L.append('DNS ERR='+repr(e))
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT,'w').write('\n'.join(L))
print('WROTE', len(L))