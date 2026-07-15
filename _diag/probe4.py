import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\out4.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    targets = [
        'build_seo_pages.py',
        'js/app.js',
        'rename_website.py',
        'setup_github_now.md',
        'ads.txt',
        'tools/age-calc/index.html',
    ]
    for t in targets:
        L.append('===== ' + t + ' =====')
        out = g(['grep', '-i', '-n', r"somar", 'HEAD', '--', t])
        L.append(out.strip()[:1500])
        L.append('')

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))