import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\out2.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    # Full commit graph
    L.append('=== LOG ALL ===')
    L.append(g(['log', '--oneline', '--all', '-20']).strip())
    L.append('=== MERGE BASE / reflog short ===')
    L.append(g(['reflog', '--oneline', '-10']).strip())

    # Secrets in current HEAD tree?
    secrets = [
        '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',
        'csk-yx4y4cfp9pmk58txe6tm8ywv5534hw566d364d3njjpyevnj',
        'fe_oa_19a7f7fcae63fe8c7d216321a5f0ae90e80012b27c76bd44',
        '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',
        '1c6533297b7118e6b29079e17585d509',
        'cfut_eQilcmOAwOwB4XAemxIKKu3HEtLKo6CF4MpvdOkbabda0c39',
        'AQ.Ab8RN6L6QaQgwsZr4uwTBWJfq9GPglW41rtWQ4LCGxGWlPNcuw',
    ]
    L.append('=== SECRETS IN HEAD TREE ===')
    for s in secrets:
        r = g(['grep', '-l', s, 'HEAD', '--'])
        L.append(f'{s[:12]}... -> {len([x for x in r.splitlines() if x.strip()])} files')

    # Secrets in ANY commit in history (all refs)
    L.append('=== SECRETS IN ANY COMMIT (all refs) ===')
    for s in secrets:
        r = g(['log', '--all', '--oneline', '-S', s])
        L.append(f'{s[:12]}... -> {len([x for x in r.splitlines() if x.strip()])} commits')

    # What are the 209 unstaged changes? Sample a diff
    L.append('=== SAMPLE UNSTAGED DIFF (index.html) ===')
    d = g(['diff', 'index.html'])
    L.append(d[:1200])

    # Does working tree still contain Somar?
    sg = g(['grep', '-l', 'Somar', '--', '*.html'])
    L.append('=== working-tree HTML files containing Somar: ' + str(len([x for x in sg.splitlines() if x.strip()])))

    # Does HEAD tree contain Somar?
    sg2 = g(['grep', '-l', 'Somar', 'HEAD', '--', '*.html'])
    L.append('=== HEAD-tree HTML files containing Somar: ' + str(len([x for x in sg2.splitlines() if x.strip()])))

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L), 'lines')