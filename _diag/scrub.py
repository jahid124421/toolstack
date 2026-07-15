import subprocess, os, traceback

R = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\mastertools-deploy'
OUT = r'c:\Users\96650\OneDrive\Desktop\AI_BA_WORKSPACE\_diag\scrub_out.txt'

L = ['start']
try:
    def g(a):
        return subprocess.run(['git', '-C', R] + a, capture_output=True, text=True).stdout

    # 1) Discard messy working-tree edits -> clean HEAD
    subprocess.run(['git', '-C', R, 'checkout', '--', '.'], capture_output=True, text=True)
    L.append('after checkout, unstaged names=' + str(len(g(['diff', '--name-only']).splitlines())))

    # 2) Replacement map (most specific first)
    reps = [
        ("Somar's All Free Tools", "ToolStack"),
        ("Somar's", "ToolStack"),
        ("Somar", "ToolStack"),
        ("somar's all free tools", "toolstack"),
        ("somar's", "toolstack"),
        ("somar", "toolstack"),
    ]

    EXCLUDE = {'rename_website.py', '_strip_somar.py'}

    tracked = [x for x in g(['ls-files']).splitlines() if x.strip()]
    changed = []
    for f in tracked:
        if f in EXCLUDE:
            continue
        p = os.path.join(R, f)
        if not os.path.isfile(p):
            continue
        try:
            with open(p, 'r', encoding='utf-8') as fh:
                data = fh.read()
        except Exception:
            # binary or non-utf8 -> skip
            continue
        if 'somar' not in data.lower():
            continue
        new = data
        for a, b in reps:
            new = new.replace(a, b)
        if new != data:
            with open(p, 'w', encoding='utf-8') as fh:
                fh.write(new)
            changed.append(f)

    L.append('files changed by replacement=' + str(len(changed)))
    L.append('changed sample=' + repr(changed[:10]))

    # 3) Verify remaining somar in served/tracked files (excluding excluded utils)
    rem = g(['grep', '-i', '-l', 'somar', '--'])
    rem_files = [x for x in rem.splitlines() if x.strip() and x.strip() not in EXCLUDE]
    L.append('remaining somar files (excl utils)=' + str(len(rem_files)))
    L.append('remaining=' + repr(rem_files[:30]))

except Exception as e:
    L.append('FATAL=' + traceback.format_exc())

open(OUT, 'w').write('\n'.join(L))
print('WROTE', len(L))