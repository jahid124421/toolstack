import urllib.request, traceback

OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\live_out.txt'
L = ['start']
try:
    urls = [
        'https://toolstack.dpdns.org/',
        'https://toolstack.dpdns.org/tools/age-calc/',
    ]
    for u in urls:
        L.append('=== ' + u + ' ===')
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')
            L.append('len=' + str(len(html)))
            L.append('ToolStack count=' + str(html.lower().count('toolstack')))
            L.append('Somar count=' + str(html.lower().count('somar')))
            # show title and og:site_name
            import re
            for m in re.findall(r'<title>[^<]*</title>', html)[:1]:
                L.append('TITLE: ' + m)
            for m in re.findall(r'og:site_name" content="[^"]*"', html)[:1]:
                L.append('OG: ' + m)
        except Exception as e:
            L.append('ERR=' + repr(e))
except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))