import shlex
import subprocess
import sys
from pathlib import Path

import jinja2


def resolve_secret(attribute: str, secret_path: str) -> str:
    gopass_cmd = ['gopass', 'show']
    if attribute == 'password':
        gopass_cmd += ['--password', secret_path]
    else:
        gopass_cmd += [secret_path, attribute]

    outcome = subprocess.run(gopass_cmd, stdout=subprocess.PIPE)

    if outcome.returncode == 0:
        return outcome.stdout.decode('utf-8')
    else:
        print('Failed to resolve secret with SC: {}'.format(outcome.returncode), file=sys.stderr)
        print(' '.join(shlex.quote(part) for part in gopass_cmd), file=sys.stderr)
        sys.exit(2)


def substitude_secrets(content: str) -> str:
    jenv = jinja2.Environment(undefined=jinja2.StrictUndefined, loader=jinja2.BaseLoader())
    template = jenv.from_string(content)
    fields = {'gp': resolve_secret}
    return template.render(**fields)


def resolve_file(file_input: Path) -> str:
    with file_input.open('r') as in_stream:
        content = in_stream.read()

    print(substitude_secrets(content))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        infile = Path(sys.argv[1])
        resolve_file(infile)
