import re
import sys
import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
OUTPUT_FILE = "adguard_temp.txt"

def convert_syntax(line):
    line = line.strip()
    
    # コメント・空行はそのまま維持
    if not line or line.startswith("!"):
        return line

    # 1. スクリプトレットの変換: ##+js(script-name, arg1, arg2...) -> #%#//scriptlet("script-name", "arg1", "arg2"...)
    scriptlet_match = re.search(r'^(.*?)##\+js\((.*?)\)$', line)
    if scriptlet_match:
        domain = scriptlet_match.group(1)
        args_raw = scriptlet_match.group(2).split(',')
        script_name = args_raw[0].strip()
        args = [f'"{a.strip()}"' for a in args_raw[1:] if a.strip()]
        
        args_str = f', {", ".join(args)}' if args else ''
        return f'{domain}#%#//scriptlet("{script_name}"{args_str})'

    # 2. 基本修飾子の正規化 ( AdGuard標準構文へ準拠 )
    if '$' in line and not line.startswith('/'):
        parts = line.split('$')
        rule = parts[0]
        modifiers = parts[1].split(',')
        
        new_mods = []
        for mod in modifiers:
            mod = mod.strip()
            if mod == '3p':
                new_mods.append('third-party')
            elif mod == '~3p':
                new_mods.append('~third-party')
            elif mod == 'css':
                new_mods.append('stylesheet')
            elif mod == 'frame':
                new_mods.append('subdocument')
            elif mod == 'xhr':
                new_mods.append('xmlhttprequest')
            else:
                new_mods.append(mod)
        return f"{rule}${','.join(new_mods)}"

    return line

def main():
    print(f"Fetching source from {SOURCE_URL}...")
    with urllib.request.urlopen(SOURCE_URL) as response:
        content = response.read().decode('utf-8')

    lines = content.splitlines()
    converted_lines = []

    print("Converting rules to AdGuard syntax...")
    for line in lines:
        converted = convert_syntax(line)
        if converted:
            converted_lines.append(converted)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted_lines) + '\n')
    print(f"Temporary file saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
