import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\verify_out.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    L.append('unstaged names=' + str(len(g(['diff', '--name-only']).splitlines())))
    L.append('diff --stat lines=' + str(len(g(['diff', '--stat']).splitlines())))

    # sanity: ensure no 'ToolStack' double-ups or 'Somar' leftovers
    L.append('any somar left=' + str(len([x for x in g(['grep', '-i', '-l', 'somar', '--']).splitlines() if x.strip()])))

    # sample build_seo_pages.py branding lines
    L.append('=== build_seo_pages.py BRAND line ===')
    L.append(g(['grep', '-n', 'BRAND', 'build_seo_pages.py']).strip())
    L.append('=== sample tool page title/footer ===')
    L.append(g(['grep', '-n', 'ToolStack', 'tools/age-calc/index.html']).strip()[:800])

    # check the previously-broken robots.txt domain
    L.append('=== robots.txt ===')
    L.append(g(['show', 'HEAD:robots.txt']).strip())
    L.append('--- working robots.txt ---')
    L.append(open(os.path.join(R,'robots.txt')).read().strip())

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))